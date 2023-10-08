import React from "react";
import StockImage from '../Assets/test.jpg'
import Robo from '../Assets/robo.png'
import { useNavigate } from 'react-router-dom';
import {toast} from "react-toastify"
import { auth } from '../firebase/firebase';
import {
    createUserWithEmailAndPassword,
    updateProfile,
    signInWithEmailAndPassword,
    sendPasswordResetEmail,
} from 'firebase/auth';

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

    const navigate = useNavigate();

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

    async function userLogin(){

        try
        {const userCredential = await signInWithEmailAndPassword(
            auth,
            signinData.email,
            signinData.password
        )

        if(userCredential.user){
            toast.success("You are successfully signed in!");
            navigate('/home');
        }
        else{
            toast.error("Bad User Credential")
        }}
        catch(error){
            let message = (error.message.split('/')[1]);
            if(message === 'wrong-password).'){
                toast.error('Incorrect Password. Try Again')
            }
            else if(message === 'user-not-found).'){
                toast.error("User Not Found")
            }
            else if(message === "network-request-failed)."){
                toast.error("Network Error")
            }
            else{
                toast.error("Something went wrong")
            }
        }

    }

    async function userSignUp(){

        try{
            await createUserWithEmailAndPassword(
                auth,
                registerData.email,
                registerData.password
            );
    
            updateProfile(auth.currentUser, {
                displayName:registerData.name
            })
    
            toast.success("You are Successfully Registered!")
            navigate('/home');
        }
        catch(error){
            toast.error("Something went wrong");
        }

    }


    async function handlePasswordReset(){
        if(!signinData.email){
            return toast.error('Email is required');
        }
        try {
          // Send a password reset email using Firebase Auth
          await sendPasswordResetEmail(auth, signinData.email);
          toast.success('Password reset email sent! Check your inbox.');
        } catch (error) {
          toast.error('Password reset failed. Please try again.');
        }
      };

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

                        <div style={{display:'flex',width:'75%',marginTop:"10px"}}>
                            <p style = {{textAlign:"left"}} onClick={handlePasswordReset}>Forgot Password?</p>
                            <p onClick={() => setForm('signup')}>New User?</p>
                        </div>
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