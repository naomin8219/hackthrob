import base64
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import requests

app = Flask(__name__)
CORS(app)
db = psycopg2.connect("postgresql://root:admin@localhost:26257")


spotify_key = "764915ada4714643a561bb17286a9882:5f33e816137f43c2979824f69987c63e"
key_bytes = spotify_key.encode("ascii")
key_b64 = base64.b64encode(key_bytes)
key_repr = key_b64.decode("ascii")
auth = "Basic " + key_repr
auth_key = ""
yelp_key = "LKt3SL1aXzuBfor6Xyn2jN8deazE732T6pvP_IP_giFdq12CLcjGe6dvQSrva6_zUQrXdnIISgof9kuYkoGHDOjhlMoYA9vqb_3OwIq7su6-gGtiMtr5erKNNE0oYHYx"

def create_dates_table():
    with db.cursor as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS dates (musicGenre int, movieGenre int, foodType int, musicLink varchar(255), movieName varchar(255), sucess bool)")
    db.commit()

def authorize_spotify():
    headers = {
        "Authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = [("grant_type", "client_credentials")]
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        headers=headers,
        data=payload
    )
    return r.json()["access_token"]

@app.route("/get-song")
def get_song():
    genre = request.json['genre']
    url  = f'https://api.spotify.com/v1/search?q=${genre} playlist&type=playlist&limit=5'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + auth_key
    }
    r = requests.get(url, headers=headers)
    items = r.json()['playlists']['items']
    playlist = items[0]["external_urls"]["spotify"]
    return jsonify({"songLink":url})

@app.route("/get-movie")
def get_movie():
    genre = request.json['genre']
    query = '''
query ($id: Int, $page: Int, $perPage: Int, $genre: String) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (id: $id, genre: $genre) {
            id
            title {
                romaji
            }
        }
    }
}
'''
    url = 'https://graphql.anilist.co'
    variables = {
        'genre': genre,
        'page': 1,
        'perPage': 1
    }
    response = requests.post(url, json={'query': query, 'variables': variables})
    name = response["data"]['media'][0]['title']['romanji']
    return jsonify({"movieName": name})

@app.route("/get-restaurant")
def get_restaurant():
    foodType = request.json["foodType"]
    location = request.json["location"]
    url = f'https://api.yelp.com/v3/businesses/search?categories={foodType}&location={location}'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {yelp_key}"
    }
    r = requests.get(url, headers=headers)
    business = r.json()['businesses'][0]
    return jsonify({
        "urlLink": business["url"],
        "name": business["name"]
    })

@app.route("/add-date", methods=["POST"])
def add_date():
    date = request.json
    command = f"INSERT INTO dates (musicGenre, movieGenre, foodType, musicLink, movieName, success) VALUES ({date['musicGenre']}, {date['movieGenre']}, {date['foodType']},'{date['musicLink']}', '{date['movieName']}', {date['success']})"
    with db.cursor as cur:
        cur.execute(command)
    db.commit()

if __name__ == "__main__":
    create_dates_table()
    auth_key = authorize_spotify()
    app.run(host="localhost", port=8000, debug=True)
