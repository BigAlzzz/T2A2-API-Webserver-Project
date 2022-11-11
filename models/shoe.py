from init import ma, db
from marshmallow import fields
from models.condition import ConditionSchema
from models.size import SizeSchema


# class Shoe(db.Model):
#     __tablename__ = 'shoes'

#     id = db.Column(db.Integer, primary_key=True)
#     brand = db.Column(db.String(100))
#     name = db.Column(db.String, nullable=False)
#     description = db.Column( db.Text)
#     release_date = db.Column(db.Date)

#     condition_id = db.Column(db.Integer)
#     size_id = db.Column(db.Integer)

class ShoeSchema(ma.Schema):
    condition = fields.Nested(ConditionSchema)
    size = fields.Nested(SizeSchema)



    class Meta:
        fields = ('id', 'brand', 'name', 'description', 'release_date', 'condition', 'size')
        ordered = True