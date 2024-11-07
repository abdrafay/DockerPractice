# basic flask hello world
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Checking ci/cd pipeline checking if everythign works perfectly'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

