import React from "react";
import StockVector from "../../Assets/8432.jpg"
import { Data } from "./Data";
import PieChart from './PieChart'
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";
import Axios from "axios"
import { toast } from "react-toastify";
import { useEffect, useState } from "react";
Chart.register(CategoryScale);

export default function Home() {

    const [topGainers, setTopGainers] = useState([]);
    const [topLosers, setTopLosers] = useState([]);
    const [responseData, setResponseData] = useState([]); 

    useEffect(() => {
        Axios.get('https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo')
        .then((response) => {
            const { top_gainers, top_losers } = response.data;

            // Update the state with the fetched data
            setTopGainers(top_gainers.slice(0, 3));
            setTopLosers(top_losers.slice(0, 3));

            toast.success('Data fetched successfully');
        })
        .catch((error) => {
            console.log(error);
            toast.error('Error in fetching data');
            // Handle the error
        });
    }, []); // The empty dependency array means this effect runs once after the initial render

    useEffect(() => {

        if(topGainers.length === 0 || topLosers.length === 0) return;

        // get the data using ticker symbol

        const tickers = [...topGainers, ...topLosers].map((stock) => stock.ticker);
        console.log(tickers)

        // making request to get the data using each ticker symbol

        tickers.forEach(element => {
            console.log("Making request for http://127.0.0.1:5000/data_chart/" + element)
            Axios.get('http://127.0.0.1:5000/data_chart/' + element)
            .then((response) => {
                console.log(response.data)
            })
        });

    },[topGainers, topLosers])

    const [chartData, setChartData] = React.useState({
        labels: Data.map((data) => data.year), 
        datasets: [
          {
            label: "Users Gained ",
            data: Data.map((data) => data.userGain),
            backgroundColor: [
              "rgba(75,192,192,1)",
              "#ecf0f1",
              "#50AF95",
              "#f3ba2f",
              "#2a71d0"
            ],
            borderColor: "black",
            borderWidth: 2
          }
        ]
      });

    return(
        <div className="Home">
            <div style={{display:'flex',height:"80vh"}}>
                <div className="home-header">
                    <h1>What do we do?</h1>
                    <p>
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maiores quae, harum soluta quis ipsum voluptatibus quos ad autem incidunt, dicta dignissimos! At nemo dicta omnis quas nisi corrupti architecto et.
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi eveniet hic quod repudiandae praesentium voluptates cupiditate. Corrupti excepturi inventore eos eaque veritatis vel modi, dicta sequi voluptas pariatur ex maiores?
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi eveniet hic quod repudiandae praesentium voluptates cupiditate. Corrupti excepturi inventore eos eaque veritatis vel modi, dicta sequi voluptas pariatur ex maiores?
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi eveniet hic quod repudiandae praesentium voluptates cupiditate. Corrupti excepturi inventore eos eaque veritatis vel modi, dicta sequi voluptas pariatur ex maiores?
                    </p>
                    
                </div>

                <img src={StockVector} alt="" />
            </div>
            
            <div className="home-header">
                <h1>What's Trending?</h1>
                <PieChart chartData={chartData} />
            </div>

        </div>
    )

}

