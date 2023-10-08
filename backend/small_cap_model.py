import pandas as pd
import requests
from arch import arch_model
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def garch_x_model(df):
    model = arch_model(
        df['Close'], x=df[['Volume', 'High', 'SMA', 'EMA']], vol='Garch')
    result = model.fit(disp='off')
    return result.conditional_volatility


def cal_volatility(symbol, key="RX10ZG3VHVU5UMXC"):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&outputsize=full'.format(
        symbol, key)
    url_sma = 'https://www.alphavantage.co/query?function=SMA&symbol={}&interval=daily&time_period=10&series_type=open&apikey={}'.format(
        symbol, key)
    url_ema = 'https://www.alphavantage.co/query?function=EMA&symbol={}&interval=daily&time_period=10&series_type=open&apikey={}'.format(
        symbol, key)

    r = requests.get(url)
    data = r.json()
    time_series_data = data['Time Series (Daily)']

    # Transpose the DataFrame to have dates as rows
    df = pd.DataFrame(time_series_data).T
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df.apply(pd.to_numeric)  # Convert columns to numeric
    df['Date'] = pd.to_datetime(df.index)

    r = requests.get(url_ema)
    data = r.json()

    # Extract 'Technical Analysis: SMA' data
    ema_data = data['Technical Analysis: EMA']
    ema_df = pd.DataFrame(ema_data).T
    ema_df.columns = ['EMA']
    ema_df['EMA'] = ema_df['EMA'].astype(float)

    ema_df.reset_index(inplace=True)
    ema_df.rename(columns={'index': 'Date'}, inplace=True)

    # print(ema_df)

    r = requests.get(url_sma)
    data = r.json()

    sma_data = data['Technical Analysis: SMA']
    sma_df = pd.DataFrame(sma_data).T
    sma_df.columns = ['SMA']
    sma_df['SMA'] = sma_df['SMA'].astype(float)
    sma_df.reset_index(inplace=True)
    sma_df.rename(columns={'index': 'Date'}, inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])
    sma_df['Date'] = pd.to_datetime(sma_df['Date'])
    ema_df['Date'] = pd.to_datetime(ema_df['Date'])
    merged_df = pd.merge(df, ema_df, on='Date', how='inner')
    merged_df = pd.merge(merged_df, sma_df, on='Date', how='inner')

    # print(merged_df)

    # Step 1: Apply GARCH-X model to predict volatility
    volatility = garch_x_model(merged_df)

    # Append volatility to 'merged_df'
    merged_df['Volatility'] = volatility

    # Step 2: Split data into train and test sets
    train_df, test_df = train_test_split(merged_df, test_size=0.2)

    # Step 3: Train an XGBoost model
    xgb_model = XGBRegressor(objective='reg:squarederror')
    x_train = train_df[['Close', 'Volatility']]
    x_test = test_df[['Close', 'Volatility']]
    y_train = train_df['Close']
    y_test = test_df['Close']

    xgb_model.fit(x_train, y_train)

    # Predict closing prices using XGBoost
    y_pred = xgb_model.predict(x_test)

    # Calculate RMSE
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    last_date = merged_df['Date'][0]
    # Generate 10 future dates starting from the next business day
    future_dates = pd.date_range(last_date, periods=11, freq='B')[1:]
    # Assuming last 20 days are available for prediction
    future_volatility = garch_x_model(merged_df)
    if len(future_dates) > len(future_volatility):
        future_dates = future_dates[:-1]
    future_features = pd.DataFrame({
        'Close': [merged_df['Close'].iloc[-1]] * len(future_dates),
        'Volatility': future_volatility,
    }, index=future_dates)
    predicted_closing_prices = xgb_model.predict(future_features)

    predicted_closing_price = predicted_closing_prices[-1]
    predicted_date = future_dates[-1]

    result = {
        "merged_df": merged_df.to_dict(),
        "predicted_closing_price": predicted_closing_price,
        "predicted_date": predicted_date.strftime('%Y-%m-%d')
    }

    return result


# print(type(cal_volatility('PTIX', 'P3B4DV2OFJBH60IG')))
