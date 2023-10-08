import requests


def get_data(function, symbol):
    # TODO: bollinger bands and stoc
    URLS = {
        "SMA": "https://www.alphavantage.co/query?function=SMA&symbol={}&interval=weekly&time_period=10&series_type=open&apikey=RX10ZG3VHVU5UMXC",
        "RSI": 'https://www.alphavantage.co/query?function=RSI&symbol={}&interval=weekly&time_period=10&series_type=open&apikey=RX10ZG3VHVU5UMXC',
        "ATR": 'https://www.alphavantage.co/query?function=ATR&symbol={}&interval=daily&time_period=14&apikey=demo',
        "OBV": 'https://www.alphavantage.co/query?function=OBV&symbol={}&interval=weekly&apikey=demo',
        "ROC": 'https://www.alphavantage.co/query?function=ROC&symbol={}&interval=weekly&time_period=10&series_type=close&apikey=demo'
    }

    d = requests.get(URLS[function.upper()].format(symbol)).json()[
        f"Technical Analysis: {function.upper()}"]

    return [{"date": k, "val": float(v[function.upper()])} for k, v in d.items()]
