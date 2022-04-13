from application import db
from datetime import date

class Stage_Name(db.model):
    id = db.Column(db.integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Festival_id = db.Column(db.integer, db.ForeignKey('Festival.id'), nullable = True)


class Festival_Name(db.model):
    id = db.Column(db.integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Start_Date = db.Column(db.Date, nullable=False)
    End_Date = db.Column(db.Date, nullable=False)
    Stages = db.relationship('Stages', backref = 'Festival')
