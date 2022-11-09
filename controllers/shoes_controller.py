from flask import Blueprint, request
from init import db
from models.shoe import Shoe, ShoeSchema

shoes_bp = Blueprint('shoes', __name__, url_prefix='/shoes')

# The GET route endpoint
@shoes_bp.route('/')
# @jwt_required() 
def all_shoes():
    # return 'all_shoes route'
    # if not authorize():
    #   return {'error': 'You must be an admin'}, 401

    stmt = db.select(Shoe).order_by(Shoe.id.desc())
    shoes = db.session.scalars(stmt)
    return ShoeSchema(many=True).dump(shoes)

@shoes_bp.route('/<int:id>/')
def one_shoe(id):
    stmt = db.select(Shoe).filter_by(id=id)
    shoe = db.session.scalar(stmt)
    if shoe:
        return ShoeSchema().dump(shoe)
    else:
        return {'error': f'shoe not found with id {id}'}, 404

@shoes_bp.route('/', methods=['POST']) # POST for creation
# @jwt_required()
def create_shoe():
    # create a new card model instance
    shoe = Shoe(
        brand = request.json['brand'],
        name = request.json['name'],
        description = request.json['description'],
        release_date = request.json['release_date'],
        condition_id =request.json['condition_id'],
        size_id =request.json['size_id']
        )    # Add and commit user to DB
    db.session.add(shoe)
    db.session.commit()
    # Return the user to check the request was successful
    return ShoeSchema().dump(shoe), 201
    