import pandas as pd
import requests
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=PTIX&apikey=P3B4DV2OFJBH60IG&outputsize=full'
r = requests.get(url)
data = r.json()
print(data)
# Extract the time series data
time_series_data = data['Weekly Time Series']

# Convert the data to a pandas DataFrame
df = pd.DataFrame(time_series_data).T  # Transpose the DataFrame to have dates as rows

# Rename the columns for better clarity
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# Convert the data types to appropriate types
df = df.apply(pd.to_numeric)  # Convert columns to numeric

# Add a 'Date' column and set it as the index
df['Date'] = pd.to_datetime(df.index)

def large_cap(data):
  
  # AutoARIMA modeling
  # Perform a stepwise search to find the best SARIMA model
  model = auto_arima(data['Close'], seasonal=True, m=7, trace=True,seasonal_test='ocsb',error_action='ignore',suppress_warnings=True,stepwise=True)
  
  # Print the model summary
  print(model.summary())
  
  # Fit the model
  model.fit(data['Close'])
  
  # Forecast future closing prices
  future_steps = 50 # Replace with the desired number of future steps
  forecast = model.predict(n_periods=future_steps)

  return forecast, data
