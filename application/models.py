from application import db
from datetime import date



class Festivals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Start_Date = db.Column(db.Date, nullable=False)
    End_Date = db.Column(db.Date, nullable=False)
    Stages = db.relationship('Stages', backref = 'festivals')


class Stages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Festival_id = db.Column(db.Integer, db.ForeignKey('festivals.id'), nullable =True )


