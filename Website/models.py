from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Upload(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    remarks=db.Column(db.String(10000))
    test_id=db.Column(db.String(10000))
    COcold=db.Column(db.Float )
    HCcold=db.Column(db.Float )
    NOxcold=db.Column(db.Float )
    NMHCcold=db.Column(db.Float )
    CO2cold=db.Column(db.Float )
    FEcold=db.Column(db.Float )
    COhot=db.Column(db.Float )
    HChot=db.Column(db.Float )
    NOxhot=db.Column(db.Float )
    NMHChot=db.Column(db.Float )
    CO2hot=db.Column(db.Float )
    FEhot=db.Column(db.Float )
    COfinal=db.Column(db.Float )
    HCfinal=db.Column(db.Float )
    NOxfinal=db.Column(db.Float )
    Rider=db.Column(db.String(100))
    NMHCfinal=db.Column(db.Float )
    CO2final=db.Column(db.Float )
    FEfinal=db.Column(db.Float )
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'))
    Vehicle= db.relationship('Vehicle')


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    uploads= db.relationship('Upload')


class Vehicle(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    engno=db.Column(db.String(100))
    frmno=db.Column(db.String(100))
    model_name=db.Column(db.String(100))
    test_id= db.Column(db.String(100),db.ForeignKey('upload.test_id'))
    tests= db.relationship('Test')

class Test(db.Model):
    test_id = db.Column(db.String(100),primary_key=True)
    date=db.Column(db.String(100))
    vehicle_id= db.Column(db.Integer,db.ForeignKey('vehicle.id'))
    RH=db.Column(db.Float )
    DBT=db.Column(db.Float )
    NOXFAC=db.Column(db.Float )

