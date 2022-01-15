
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


@app.route('/poems/<author>', methods=['GET'])
@app.route('/poems/', methods=['GET'])
def poems(author=None, title=None):

    if author:
        poems = []
        for poem in Poem.select().where(Poem.author == author):
            poem = model_to_dict(poem)
            poems.append(poem)
        poems = jsonify(poems)
        return poems
    else:
        poems = []
        for poem in Poem.select():
            poem = model_to_dict(poem)
            poems.append(poem)
        poems = jsonify(poems)
        return poems


@app.route('/title/<title>', methods=['GET'])
def title(title=None):
    if title:
        poems = []
        for poem in Poem.select().where((Poem.title % f'%{title.capitalize()}%') | (Poem.title % f'%{title}%')):
            poem = model_to_dict(poem)
            poems.append(poem)

        if poems == []:
            return jsonify({'Message': "No Poem's Title Contains those Letters In that Order"})
        else:
            poems = jsonify(poems)
            return poems


app.run(port=9000, debug=True)
