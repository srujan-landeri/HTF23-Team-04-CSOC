from flask import Flask, request, jsonify
from data_processing import get_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/data_chart/<string:func>/<string:symbol>')
def data_chart(func, symbol):
    return jsonify(get_data(func, symbol))


if __name__ == '__main__':
    app.run(debug=True)
