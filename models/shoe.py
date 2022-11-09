from init import ma, db
from marshmallow import fields

class Shoe(db.Model):
    __tablename__ = 'shoes'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    name = db.Column(db.String)
    description = db.Column( db.Text)

    condition_id = db.Column(db.Integer)
    size_id = db.Column(db.Integer)