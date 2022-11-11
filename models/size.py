from init import ma, db
from marshmallow import fields

class Size(db.Model):
    __tablename__ = 'sizes'

    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    shoes = db.relationship('Shoe', back_populates='size')


class SizeSchema(ma.Schema):
    class Meta:
        fields = ('size', 'gender')
        ordered = True