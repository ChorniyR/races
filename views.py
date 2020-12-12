from flask import Blueprint, render_template, request

from forms import HorseForm, JockeyForm, ParticipationForm
from models import Horse, Jockey, Competition, Participition

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home_page():
    return render_template("index.html")


@page.route('/horses', methods=['GET', 'POST'])
def horses():
    form = HorseForm(request.form)
    horses = Horse.query.all()
    form.save(request.method)
    return render_template('horses.html', horses=horses, form=form)


@page.route('/horses_sorted', methods=['GET', 'POST'])
def horses_sorted():
    form = HorseForm(request.form)
    horses = Horse.query.order_by(Horse.win_score)
    form.save(request.method)
    return render_template('horses.html', horses=horses, form=form)


@page.route('/horses_sorted_rev', methods=['GET', 'POST'])
def horses_sorted_rev():
    form = HorseForm(request.form)
    horses = Horse.query.order_by(Horse.win_score.desc())
    form.save(request.method)
    return render_template('horses.html', horses=horses, form=form)


@page.route('/jockeys', methods=['GET', 'POST'])
def jockeys():
    form = JockeyForm(request.form)
    jockeys = Jockey.query.all()
    form.save(request_method=request.method)
    return render_template('jockeys.html', jockeys=jockeys, form=form)


@page.route('/jockeys_sorted', methods=['GET', 'POST'])
def jockeys_sorted():
    form = JockeyForm(request.form)
    jockeys = Jockey.query.order_by(Jockey.win_score)
    form.save(request_method=request.method)
    return render_template('jockeys.html', jockeys=jockeys, form=form)


@page.route('/jockeys_sorted_rev', methods=['GET', 'POST'])
def jockeys_sorted_rev():
    form = JockeyForm(request.form)
    jockeys = Jockey.query.order_by(Jockey.win_score.desc())
    form.save(request_method=request.method)
    return render_template('jockeys.html', jockeys=jockeys, form=form)


@page.route('/events', methods=['GET', 'POST'])
def events():
    form = ParticipationForm(request.form)
    partitipitions = Participition.query.join(Competition)
    form.save(request.method)
    return render_template('events.html', partitipitions=partitipitions, form=form)
