import requests
from peewee import *
from playhouse.postgres_ext import *

response_API = requests.get(
    'https://poetrydb.org/author/Dickinson')
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
db.drop_tables([Poem])
db.create_tables([Poem])

# print(data)

for poem in data:
    #     print(len(poem))
    lines = list(poem['lines'])
    print(lines)

    poem = Poem(title=poem['title'], author=poem['author'],
                linecount=poem['linecount'], lines=lines)
    poem.save()
