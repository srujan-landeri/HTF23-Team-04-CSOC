from flask import Flask, request, jsonify
from data_processing import get_data, choose_model
from small_cap_model import cal_volatility
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# http://127.0.0.1:5000/data_chart/IBM
@app.route('/data_chart/<string:symbol>')
# http://127.0.0.1:5000/data_chart/IBM/SMA
@app.route('/data_chart/<string:symbol>/<string:func>')
def data_chart(symbol, func=None):
    return jsonify(get_data(symbol, func))

# for model return


@app.route('/model/<string:symbol>')
def model(symbol):
    chosed_model = choose_model(symbol)
    # print(chosed_model)
    if chosed_model == "small_cap":
        res = cal_volatility(symbol.upper())
        df = res["merged_df"]
        # pandas df to json
        return [{"date": k, "val": v} for k, v in df["Close"].items()]

    return "Npoe"
    # result of model should be in json format, (list of objects)

    # return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
