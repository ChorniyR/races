from flask_wtf import FlaskForm as Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, SubmitField

from models import Jockey, Horse, Competition, Participition


def get_all_jockeys():
    return Jockey.query.all()


def get_all_horses():
    # return [horse for horse in Jockey.horses]
    return Horse.query.all()


def get_all_cometitions():
    return Competition.query.all()


class JockeyForm(Form):
    name = StringField('Имя')
    age = IntegerField('Возраст')
    submit = SubmitField('Submit')

    def save(self, request_method):
        if request_method == 'POST':
            name = self.name.data
            age = self.age.data
            Jockey.save(Jockey(name=name, age=age, win_score=0))


class HorseForm(Form):
    name = StringField('Имя')
    age = IntegerField('Возраст')
    jockey = QuerySelectField("Жокей", query_factory=get_all_jockeys)
    suit = StringField('Масть')
    submit = SubmitField('Submit')

    def save(self, request_method):
        if request_method == "POST":
            name = self.name.data
            age = self.age.data
            suit = self.suit.data
            jockey_id = self.jockey.data.id
            Horse.save(Horse(name=name, age=age, suit=suit, jockey_id=jockey_id, win_score=0))

    def __repr__(self):
        return f"HorseForm({self.name},{self.age},{self.submit})"


class ParticipationForm(Form):
    place = StringField('Место')
    horse = QuerySelectField('Лошадь', query_factory=get_all_horses)
    jockey = QuerySelectField('Жокей', query_factory=get_all_jockeys)
    competition = QuerySelectField('Соревнование', query_factory=get_all_cometitions)
    submit = SubmitField('Submit')

    def save(self, request_method):
        if request_method == 'POST':
            place = self.place.data
            horse = self.horse.data
            jockey = self.jockey.data
            competition = self.competition.data
            Participition.save(
                Participition(place=place, horse_id=horse.id, jockey_id=jockey.id, competition_id=competition.id))


