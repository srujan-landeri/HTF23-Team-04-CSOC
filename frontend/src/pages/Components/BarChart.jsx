// src/components/BarChart.js
import React from 'react';
import { Bar } from 'react-chartjs-2';

const BarChart = ({data}) => {
  return (
    <div>
      <Bar data={data} 
      
      options={{
          plugins: {
            title: {
              display: true,
              text: "Users Gained between 2016-2020"
            }
          }
        }} />
    </div>
  );
};

export default BarChart;
