from __future__ import annotations
from flask import Flask, Response, request
from jsonclasses_pymongo import Connection
from jsonclasses_flask import jsonclasses_integrate, data, empty, encode_jwt_token
from models.statement import Statement
from models.item import Item
from utils.jsjson_encoder import JSJSONEncoder
from utils.data import data
from utils.empty import empty


app = Flask(__name__)

app.json_encoder = JSJSONEncoder

app.url_map.strict_slashes = False

jsonclasses_integrate(app, cors={
    'allow_headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
}, operator={
    'operator_cls': Statement,
    'encode_key': 'SECRET_VERY_SECRET'
})

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')