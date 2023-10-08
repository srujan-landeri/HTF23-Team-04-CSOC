// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCSL2Eg6UqPTlwuegdwnW3VbavurslMuDg",
  authDomain: "stocks-d91bd.firebaseapp.com",
  projectId: "stocks-d91bd",
  storageBucket: "stocks-d91bd.appspot.com",
  messagingSenderId: "958537725791",
  appId: "1:958537725791:web:fc1e8a4a95be28f14468ea"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app)