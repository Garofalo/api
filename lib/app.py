
from distutils.log import debug
from peewee import *
from playhouse.postgres_ext import *
from flask import jsonify
from flask import Flask
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.postgres_ext import *


db = PostgresqlDatabase('poems', user='postgres',
                        password='password', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Poem(BaseModel):
    title = CharField()
    author = CharField()
    linecount = CharField()
    lines = ArrayField(CharField)


db.connect()

app = Flask(__name__)


@app.route('/poems', methods=['GET'])
def poems(id=None):
    poems = []
    for poem in Poem.select():
        poem = model_to_dict(poem)
        poems.append(poem)
    poems = jsonify(poems)
    return poems


app.run(port=9000, debug=True)
