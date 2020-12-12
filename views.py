from flask import Blueprint, render_template, request

from forms import HorseForm, JockeyForm, ParticipationForm, FindByDateForm, FindByHorseForm, FindByJockeyForm
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
    date_form = FindByDateForm(request.form)
    horses_form = FindByHorseForm(request.form)
    form = ParticipationForm(request.form)
    jockeys_form = FindByJockeyForm(request.form)

    partitipitions = Participition.query.join(Competition)

    if request.method == "POST":
        if date_form.date.data:
            partitipitions = Participition.query.join(Competition).filter(Competition.date == date_form.date.data,
                                                                          Participition.place == 1)
        if horses_form.horse.data:
            partitipitions = Participition.query.join(Competition).filter(Participition.horse == horses_form.horse.data)

        if jockeys_form.jockey.data:
            partitipitions = Participition.query.join(Competition).filter(Participition.jockey == jockeys_form.jockey.data)

        if form.data and form.validate_on_submit():
            form.save()
    return render_template('events.html', partitipitions=partitipitions, form=form, date_form=date_form,
                           horse_form=horses_form, jockeys_form=jockeys_form)
