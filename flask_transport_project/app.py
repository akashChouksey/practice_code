from flask import Flask,abort

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    abort(429)


if __name__ == '__main__':
    app.run(debug=True)
