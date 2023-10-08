import requests
from json import load

FILE = "../data/{}.json"

with open(FILE.format("large_cap"), "r") as f:
    LARGE_CAP = load(f)["data"]

with open(FILE.format("medium_cap"), "r") as f:
    MID_CAP = load(f)["data"]

with open(FILE.format("small_cap"), "r") as f:
    SMALL_CAP = load(f)["data"]


def get_data(symbol, function=None):
    # TODO: bollinger bands and stoc
    URLS = {
        "SMA": "https://www.alphavantage.co/query?function=SMA&symbol={}&interval=weekly&time_period=10&series_type=open&apikey=RX10ZG3VHVU5UMXC",
        "RSI": 'https://www.alphavantage.co/query?function=RSI&symbol={}&interval=weekly&time_period=10&series_type=open&apikey=RX10ZG3VHVU5UMXC',
        "ATR": 'https://www.alphavantage.co/query?function=ATR&symbol={}&interval=daily&time_period=14&apikey=demo',
        "OBV": 'https://www.alphavantage.co/query?function=OBV&symbol={}&interval=weekly&apikey=demo',
        "ROC": 'https://www.alphavantage.co/query?function=ROC&symbol={}&interval=weekly&time_period=10&series_type=close&apikey=demo'
    }

    if function is None:
        URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey=RX10ZG3VHVU5UMXC'
        d = requests.get(URL.format(symbol)).json()[
            "Weekly Time Series"]
        return [{"date": k, **v} for k, v in d.items()]

    d = requests.get(URLS[function.upper()].format(symbol)).json()[
        f"Technical Analysis: {function.upper()}"]

    return [{"date": k, "val": float(v[function.upper()])} for k, v in d.items()]


def choose_model(symbol):
    if symbol in map(lambda x: x["Symbol"], LARGE_CAP):
        return "large_cap"
    elif symbol in map(lambda x: x["Symbol"], MID_CAP):
        return "mid_cap"
    elif symbol in map(lambda x: x["Symbol"], SMALL_CAP):
        return "small_cap"
    else:
        return None
