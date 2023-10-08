import React from "react";
import {FcSearch} from "react-icons/fc";
import Forecast from "../../Assets/4101.jpg";
export default function Home() {
    return(
        <div className="Stocks">
            <img src={Forecast} alt="" />
            <div class = "stock-header">
                <div>
                    <input placeholder="Forecast your stocks" type="text" name="search" id="" />
                    <FcSearch 
                    
                    size={26}
                    style={{
                        position: "absolute",
                        top: "22px",
                        right:"12px",
                    }}/>
                </div>
            </div>
        </div>
    )
}