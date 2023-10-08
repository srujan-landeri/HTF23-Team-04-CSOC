import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def predict(data):
  # Assuming you have a univariate time series of historical stock prices
  # Here, 'data["Close"]' is a 1D array representing past stock prices
  model = load_model('gru_model.h5')
  
  sequence_length = 20  # Choose an appropriate sequence length
  num_features = 1  # For a univariate time series
  
  # Assuming 'data["Close"]' is a 1D array representing past stock prices
  # Prepare seed data by taking the last 'sequence_length' data points
  seed_data = np.array(data["Close"].iloc[-sequence_length:])
  seed_data = np.reshape(seed_data, (1, sequence_length, num_features))
  
  # Number of future time steps to forecast
  forecast_steps = 10
  
  # Forecast future prices
  predicted_prices = []
  
  for _ in range(forecast_steps):
      # Reshape the seed data to match the model's input shape
      seed_data_reshaped = np.reshape(seed_data, (1, sequence_length, num_features))
  
      # Predict the next time step
      predicted_price_scaled = model.predict(seed_data_reshaped)
      predicted_price = scaler.inverse_transform(predicted_price_scaled)
  
      # Update the seed data for the next prediction
      seed_data = np.append(seed_data[:, 1:, :], np.reshape(predicted_price, (1, 1, num_features)), axis=1)
  
      # Store the predicted price
      predicted_prices.append(predicted_price[0][0])
  
  # Display the predicted prices
  return (predicted_prices)
