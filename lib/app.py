from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('poems', user='postgres',
                        password='password', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Poem(BaseModel):
    author = CharField()
    title = CharField()
    first_line = CharField()
