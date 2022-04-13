from application import app
from flask import render_template
from application.forms import StageForm, FestivalForm



@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/New_Festival', methods=['GET', 'POST'])
def New_Festival():
    form = FestivalForm()
    return render_template('Festivals.html', form=form)


@app.route('/Add_Stage',  methods=['GET', 'POST'] )
def Add_Stage():
    form = StageForm()
    return render_template('Stages.html', form=form)

