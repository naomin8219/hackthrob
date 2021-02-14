import React, { Component } from 'react';
import './polaroid.css';
import pic from './train.jpeg';
class Polaroid extends Component{
    render(){
        return(
            <div className ="outter-box">
                <div className="tape"> </div>
                    <div className="inner-box">
                        <img src={pic}/>
                        <div className="text">
                             Date Generator
                        </div>
                        <div className="date">
                            2021-02-14
                        </div>
                    </div>
            </div>
       


        )
    }
}

export default Polaroid;
