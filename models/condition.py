from init import ma, db
from marshmallow import fields

class Condition(db.Model):
    __tablename__ = 'conditions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    shoes = db.relationship('Shoe', back_populates='condition')

class ConditionSchema(ma.Schema):
    class Meta:
        fields = ('id','name')