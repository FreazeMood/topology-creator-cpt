from flask import Flask


app = Flask(__name__)


@app.route('/create-basic-topology')
def creation():
    return 'success'


if __name__ == '__main__':
    app.run(debug=True, port=5001)