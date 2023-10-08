import React from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { auth } from "../firebase/firebase";
import Home from "./Components/Home";
import Stocks from "./Components/Stocks";
import Chatbot from "./Components/Chatbot";
import Logo from "../Assets/logo.png";

export default function HomePage() {
    
    const [tab, setTab] = React.useState("Home");
    const navigate = useNavigate();
    
    return (
        <div className="HomePage">

            <div className="main-header">
                <img src={Logo} alt="" />
                <nav>
                    <ul className={tab === "Home"? "active" : ""} onClick={() => setTab('Home')}>Home</ul>
                    <ul className={tab === "Stocks"? "active" : ""} onClick={() => setTab('Stocks')}>Stocks</ul>
                    <ul className={tab === "Chatbot"? "active" : ""} onClick={() => setTab('Chatbot')}>Chatbot</ul>
                    <ul onClick={() => navigate('/')}>Logout</ul>
                </nav>
            </div>
            
            <div className="body">
                {tab === "Home" && <Home />}
                {tab === "Stocks" && <Stocks />}
                {tab === "Chatbot" && <Chatbot />}
            </div>
                        
        </div>
    )
}
