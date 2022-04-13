from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class StageForm(FlaskForm):
    name = StringField('Stage Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Stage')




class FestivalForm(FlaskForm):
    Name = StringField('Festival Name', validators=[DataRequired(), Length(max=100)])
    Start_Date = DateField('Start Date', validators=[DataRequired()])
    End_Date = DateField('Finish Date', validators=[DataRequired()])
    submit = SubmitField('Add Festival')