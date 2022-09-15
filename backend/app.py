from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def creation():
    return 'success'


if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, port=5001)