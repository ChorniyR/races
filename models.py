from flask_wtf import FlaskForm as Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms import validators
from database import db


class Horse(db.Model):
    __tablename__ = 'horses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    age = db.Column(db.Integer)
    owner = db.Column(db.String(20))
    place = db.Column(db.String(20))
    suit = db.Column(db.String(20))
    win_score = db.Column(db.Integer)
    events = db.relationship('Event', backref='horse')

    def add_new(name, age):
        db.session.add(Horse(name=name, age=age))
        db.session.commit()

    def __repr__(self):
        return "<Horse('%s',%s','%s',%s',%s)>" % (self.name, self.age, self.owner, self.place, self.suit)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DATE)
    name = db.Column(db.String(30))
    horse_id = db.Column(db.Integer, db.ForeignKey('horses.id'), )
    jockey_id = db.Column(db.Integer, db.ForeignKey('jockeys.id'), )
    hippodrome = db.Column(db.String(20))
    score = db.Column(db.Integer)

    def __repr__(self):
        return "<Leap('%s','%s', '%s'" % (self.id, self.date, self.hippodrome)


class Jockey(db.Model):
    __tablename__ = 'jockeys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    win_score = db.Column(db.Integer)
    events = db.relationship('Event', backref='jockey')

    def __repr__(self):
        return "<Jockey(%s, %s, %s)>" % (self.id, self.name, self.age)

    def add_new(name, age):
        db.session.add(Jockey(name=name, age=age))
        db.session.commit()

class HorseForm(Form):
    name = StringField('Имя', [validators.Length(min=4, max=10)])
    age = IntegerField('Возраст',)
    submit = SubmitField('Submit')



class JockeyForm(Form):
    name = StringField('Имя', [validators.Length(min=4, max=10)])
    age = IntegerField('Возраст')
    submit = SubmitField('Submit')




