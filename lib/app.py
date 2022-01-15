
from crypt import methods
from peewee import *
from playhouse.postgres_ext import *
from flask import jsonify
from flask import Flask
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.postgres_ext import *
import random


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


@app.route('/random/<author>', methods=['GET'])
@app.route('/random/', methods=['GET'])
def random_poem(author=None):

    if author:
        poems = []
        for poem in Poem.select().where(Poem.author == author):
            poem = model_to_dict(poem)
            poems.append(poem)
        if poems == []:
            return jsonify({'Message': 'No Authors found. Remember to use full name and case sensitivity'})
        else:
            index = random.randint(1, len(poems))
            poem = poems[index]
            poem = jsonify(poem)
            return poem
    else:
        poems = Poem.select()
        index = random.randint(1, len(poems))
        poem = poems[index]
        poem = model_to_dict(poem)
        poem = jsonify(poem)
        return poem


@app.route('/lines/<line>', methods=['GET'])
@app.route('/lines/', methods=['GET'])
def lines(line=None):
    if line:
        subquery = Poem.select(
            Poem.lines,
            fn.ARRAY_AGG(Poem.lines).alias('lines')).group_by(Poem.lines)
        return 'Hi'
        # for poem in Poem.select().where(Poem.lines == line):
        #     poem = model_to_dict(poem)
        #     poems.append(poem)
        #     if poems == []:
        #         return jsonify({"Message": 'No lines contain that sequence of letters.'})
        #     else:
        #         return jsonify(poems)

    else:
        poems = Poem.select()
        index = random.randint(1, len(poems))
        poem = poems[index]
        poem = model_to_dict(poem)
        lines = poem['lines']
        rand_line_pos = random.randint(1, len(lines)-1)
        rand_line = lines[rand_line_pos]
        while rand_line == '':
            rand_line_pos = random.randint(1, len(lines)-1)
            rand_line = lines[rand_line_pos]
        rand_line = jsonify(rand_line)
        return rand_line


app.run(port=9000, debug=True)
