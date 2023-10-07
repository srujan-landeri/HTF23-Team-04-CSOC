import React from "react";
import StockImage from '../Assets/test.jpg'
import Robo from '../Assets/robo.png'

export default function WelcomePage(){
    
    const [form,setForm] = React.useState("main")

    const [signinData, setSigninData] = React.useState({
        email: "",
        password: "",
    })

    const [registerData, setRegisterData] = React.useState({
        name: '',
        email: '',
        password: ''
    })

    function handleFormChange(event) {
        if (form === "login") {
            setSigninData(prev => {
                return {
                    ...prev,
                    [event.target.name]: event.target.value
                }
            })
        }
        else {
            setRegisterData(prev => {
                return {
                    ...prev,
                    [event.target.name]: event.target.value
                }
            })
        }
    }

    function userLogin(){

        console.log(signinData)

    }

    function userSignUp(){

        console.log(registerData)

    }

    return(
        <div className="WelcomePage">
            <img className = "welcome-image" src={StockImage} alt="welcome" />
            <div className="header">
                <h1>STONKS</h1>
                <div className = "sub-header">
                    <h4>POWERED BY AI</h4>
                    <img className="robo-image" src={Robo} alt="robo" />
                </div>
                
                {form === "main" && (
                    <div>
                        <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium ab
                        placeat impedit tenetur? Vitae, qui eaque, iste quidem accusantium ea
                        atque quam sapiente debitis eum vero! Atque accusamus magni nam?
                        </p>

                        <div className="buttons-container">
                        <button onClick={() => setForm('login')} className="button login">Login</button>
                        <button onClick={() => setForm('signup')} className="button signup">Sign Up</button>
                        </div>
                    </div>
                )}

                {form === "login" && (
                    <div className="login-form">
                        <input onChange={handleFormChange} name = "email" type="email" placeholder="Email" />
                        <input onChange={handleFormChange} name = "password" type="password" placeholder="Password" />
                        <p onClick={() => setForm('signup')}>New User?</p>
                        <button onClick = {userLogin} className="button login">Login</button>
                    </div>
                )}

                {form === "signup" && (
                    <div className="signup-form">
                        <input onChange={handleFormChange} name = "name" type="text" placeholder="Username" />
                        <input onChange={handleFormChange} name = "email" type="email" placeholder="Email" />
                        <input onChange={handleFormChange} name = "password" type="password" placeholder="Password" />
                        <p onClick = {() => setForm('login')}>Already have an account?</p>
                        <button onClick = {userSignUp} className="button signup">Sign Up</button>
                    </div>
                )}
            </div>
        </div>
    );
}