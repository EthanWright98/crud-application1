from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import StageForm, FestivalForm
from application.models import Festivals, Stages
from datetime import date



@app.route('/')
@app.route('/Home')
def Home():
    all_festivals = Festivals.query.all()
    all_stages = Stages.query.all()

    return render_template('Home.html', all_festivals=all_festivals, all_stages=all_stages)

@app.route('/New_Festival', methods=['GET', 'POST'])
def New_Festival():
    form = FestivalForm()
    if request.method == "POST":
        Festival = Festivals(Name = form.Name.data, Start_Date = form.Start_Date.data, End_Date = form.End_Date.data)
        db.session.add(Festival)
        db.session.commit()
        return redirect(url_for('Add_Stage'))


    return render_template('Festivals.html', form=form)


@app.route('/Add_Stage',  methods=['GET', 'POST'] )
def Add_Stage():
    form = StageForm()
    if request.method == "POST":
        Stage = Stages(Name = form.Name.data, Festival_id = form.Festival_id.data)
        db.session.add(Stage)
        db.session.commit()
        return redirect(url_for("Home"))
    return render_template('Stages.html', form=form)

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form= FestivalForm()
    Festival= Festivals.query.filter_by(id=id).first()
    if request.method == "POST":
        Festival.Name = form.Name.data
        Festival.Start_Date = form.Start_Date.data
        Festival.End_Date = form.End_Date.data
        db.session.commit()
        return redirect(url_for("Home"))
    return render_template("Update.html", title="Update Festival Name", form=form, Festival=Festival)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    Festival= Festivals.query.filter_by(id=id).first()
    db.session.delete(Festival)
    db.session.commit()
    return redirect(url_for("Home"))

