import React, { Component } from 'react';
import './survey.css';
class Survey extends Component{
    render(){
        return(
            <div className ="outter-box">
                <div className="tape"> </div>
                 <div className="inner-box">
                     <div className="to"> To: you </div>
                     <div className="from"> From: us </div>
                     <div className="text"> What's your favorite music genre? </div>
                     <div class="custom-select">
                         <select className ="choices">
                             <option value="r&b">r&b</option>
                             <option value="kpop">kpop</option>
                             <option value="hip-hop">hip-hop</option>
                             <option value="rap">rap</option>
                             <option value="country">country</option>
                             <option value="metal">metal</option>
                         </select>
                    </div>
                     <div className ="button_">
                     <button className ="Send"> Send
                     </button>
                     </div>
                    </div>
            </div>


        )
    }
}

export default Survey;
