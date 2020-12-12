from flask_wtf import FlaskForm as Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms import validators
from database import db


class Horse(db.Model):
    __tablename__ = 'horses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    suit = db.Column(db.String(64))
    win_score = db.Column(db.Integer)
    jockey_id = db.Column(db.Integer, db.ForeignKey('jockeys.id'))

    participition = db.relationship('Participition')


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def __repr__(self):
        return "<Horse('%s',%s',%s)>" % (self.name, self.age, self.suit)


class Jockey(db.Model):
    __tablename__ = 'jockeys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    win_score = db.Column(db.Integer)

    participition = db.relationship('Participition')
    horses = db.relationship('Horse')

    def __repr__(self):
        return "<Jockey(%s, %s, %s)>" % (self.id, self.name, self.age)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


class Competition(db.Model):
    __tablename__ = 'competitions'
    id = db.Column(db.Integer, primary_key=True)
    hippodrom_id = db.Column(db.Integer, db.ForeignKey('hippodroms.id'))
    date = db.Column(db.DATE)

    participitions = db.relationship("Participition", backref="competitions")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


class Participition(db.Model):
    __tablename__ = 'participitions'
    place = db.Column(db.Integer)
    horse_id = db.Column(db.Integer, db.ForeignKey('horses.id'), primary_key=True)
    jockey_id = db.Column(db.Integer, db.ForeignKey('jockeys.id'), primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id'), primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()


    def save(self):
        db.session.add(self)
        db.session.commit()


class Hippodrome(db.Model):
    __tablename__ = 'hippodroms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(64))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()










