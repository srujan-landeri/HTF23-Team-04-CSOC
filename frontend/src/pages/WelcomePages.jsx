import React from "react";
import StockImage from '../Assets/test.jpg'
import Robo from '../Assets/robo.png'

export default function WelcomePage(){
    return(
        <div className="WelcomePage">
            <img className = "welcome-image" src={StockImage} alt="welcome" />
            <div className="header">
                <h1>STONKS</h1>
                <div className = "sub-header">
                    <h4>POWERED BY AI</h4>
                    <img className="robo-image" src={Robo} alt="robo" />
                </div>
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium ab placeat impedit tenetur? Vitae, qui eaque, iste quidem accusantium ea atque quam sapiente debitis eum vero! Atque accusamus magni nam?
                </p>

                <div className="buttons-container">
                    <button className="button login">Login</button>
                    <button className="button signup">Sign Up</button>
                </div>
            </div>
        </div>
    );
}