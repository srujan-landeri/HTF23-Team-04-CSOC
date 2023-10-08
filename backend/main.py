from flask import Flask, request, jsonify
from data_processing import get_data

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


if __name__ == '__main__':
    app.run(debug=True)
