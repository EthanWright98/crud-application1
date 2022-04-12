from application import app
from flask import render_template



@app.route('/')
def Home():
    return render_template('Home.html')