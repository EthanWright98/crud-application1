from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class StageForm(FlaskForm):
    Name = StringField('Stage Name', validators=[DataRequired(), Length(max=100)])
    Festival_id = IntegerField('Which Festival?', validators=[DataRequired()])
    submit = SubmitField('Add Stage')




class FestivalForm(FlaskForm):
    Name = StringField('Festival Name', validators=[DataRequired(), Length(max=100)])
    Start_Date = DateField('Start Date', validators=[DataRequired()])
    End_Date = DateField('Finish Date', validators=[DataRequired()])
    submit = SubmitField('Add Festival')