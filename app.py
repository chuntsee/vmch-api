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

@app.get('/statements')
async def statements() -> Response:
    return data(await Statement.find())
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.get('/statements/<id>')
async def statement(id: str) -> Response:
    return data(await Statement.id(id))


@app.post('/statements')
async def create_statement() -> Response:
    return data(Statement(**request.json).save())


@app.patch('/statements/<id>')
async def update_statement(id: str) -> Response:
    return data((await Statement.id(id)).set(**request.json).save())


@app.delete('/statements/<id>')
async def delete_statement(id: str) -> Response:
    return empty((await Statement.id(id)).delete())

@app.get('/statements/userid/<id>')
async def user_statements(id: str) -> Response:
    return data(await Statement.find(user_id=id))

@app.get('/items')
async def items() -> Response:
    return data(await Item.find())


@app.get('/items/<id>')
async def item(id: str) -> Response:
    return data(await Item.id(id))


@app.post('/items')
async def create_item() -> Response:
    return data(Item(**request.json).save())


@app.patch('/items/<id>')
async def update_item(id: str) -> Response:
    return data((await Item.id(id)).set(**request.json).save())


@app.delete('/items/<id>')
async def delete_item(id: str) -> Response:
    return empty((await Item.id(id)).delete())

if __name__ == "__main__":
	app.run(host='0.0.0.0')
