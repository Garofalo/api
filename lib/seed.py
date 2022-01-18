import requests
from peewee import *
from playhouse.postgres_ext import *

response_API = requests.get(
    'https://poetrydb.org/author/Edgar%20Allan%20Poe')
data = response_API.json()

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


for poem in data:

    lines = list(poem['lines'])
    print(lines)

    poem = Poem(title=poem['title'], author=poem['author'],
                linecount=poem['linecount'], lines=lines)
    poem.save()
