from flask_wtf import FlaskForm as Form, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, SubmitField

from models import Jockey


def get_all_jockeys():
    return Jockey.query.all()


class JockeyForm(Form):
    name = StringField('Имя')
    age = IntegerField('Возраст')
    submit = SubmitField('Submit')


class HorseForm(Form):
    name = StringField('Имя')
    age = IntegerField('Возраст')
    jockey = QuerySelectField("Жокей", query_factory=get_all_jockeys)
    submit = SubmitField('Submit')

    def __repr__(self):
        return f"HorseForm({self.name},{self.age},{self.submit})"
