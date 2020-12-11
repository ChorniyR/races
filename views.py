from flask import Blueprint, render_template, request, flash

import models

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home_page():
    return render_template("index.html")


@page.route('/horses', methods=['GET', 'POST'])
def horses():
    form = models.HorseForm(request.form)
    horses = models.Horse.query.all()
    if request.method == "POST":
        name = form.name.data
        age = form.age.data
        models.Horse.add_new(name=name, age=age)
    return render_template('horses.html', horses=horses, form=form)


@page.route('/jockeys', methods=['GET', 'POST'])
def jockeys():
    form = models.JockeyForm(request.form)
    jockeys = models.Jockey.query.all()
    if request.method == 'POST':
        name = form.name.data
        age = form.age.data
        models.Jockey.add_new(name=name, age=age)
    return render_template('jockeys.html', jockeys=jockeys, form=form)


@page.route('/events')
def events():
    events = models.Event.query.all()
    return render_template('events.html', events=events)
