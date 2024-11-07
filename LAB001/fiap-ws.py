# flask --app fiap-ws run
# https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
# www.pythonanywhare.com (Anaconda)

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    new = str(datetime.now())
    return f"<p>Hello, FIAP! - {new}</p>"

@app.route("/add/<a>/<b>")
def add_num(a, b):
    out = str(float(a)+float(b))
    return out