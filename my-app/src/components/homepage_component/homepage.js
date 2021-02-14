import React, { Component } from 'react';
import './Homepage.css';
class Homepage extends Component{
    componentDidMount(){
        document.body.classList.add('background-pink');
    }
    render(){
        return(
            <div className ="homepage">
                <div className = "title">
                    Website Name
                    <div className = "navigation">
                    <nav>
                        <ul>
                            <a href="#">Home</a>
                        </ul>
                    </nav>
                    </div>
                </div>
            </div>
        )
    }
}

export default Homepage;
