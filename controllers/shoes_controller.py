from flask import Blueprint, request
from init import db
from models.user_shoe import Shoe
from models.shoe import ShoeSchema
from models.user import UserSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    print(shoe.condition)
    if shoe:
        return ShoeSchema().dump(shoe)
    else:
        return {'error': f'shoe not found with id {id}'}, 404


# @shoes_bp.route('/<int:id>/users')
# def one_shoe(id):
#     stmt = db.select(Shoe).filter_by(id=id)
#     shoe = db.session.scalar(stmt)
#     return UserSchema(many=True).dump(shoe.users)


@shoes_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_shoe(id):
    authorize() #for admin
    stmt = db.select(Shoe).filter_by(id=id)
    shoe = db.session.scalar(stmt)
    if shoe:
        db.session.delete(shoe)
        db.session.commit()
        return {'message': f"Shoe '{shoe.name}' deleted successfully"} 
    else:
        return {'error': f'Shoe not found with id {id}'}, 404

@shoes_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_shoe(id):
    stmt = db.select(Shoe).filter_by(id=id)
    shoe = db.session.scalar(stmt)
    if shoe:
        shoe.brand = request.json.get('brand') or shoe.brand
        shoe.name = request.json.get('name') or shoe.name
        shoe.description = request.json.get('description') or shoe.description
        shoe.release_date = request.json.get('release_date') or shoe.release_date
        shoe.condition_id =request.json.get('condition_id') or shoe.condition_id
        shoe.size_id =request.json.get('size_id') or shoe.size_id
        db.session.commit()
        return ShoeSchema().dump(shoe)
    else:
        return {'error': f'shoe not found with id {id}'}, 404

@shoes_bp.route('/', methods=['POST']) # POST for creation
@jwt_required()  
def create_shoe():
    # create a new shoe model instance
    shoe = Shoe(
        brand = request.json['brand'],
        name = request.json['name'],
        description = request.json['description'],
        release_date = request.json['release_date'],
        condition_id =request.json['condition_id'],
        size_id =request.json['size_id']
        )    
    db.session.add(shoe)
    db.session.commit()
    # Return the user to check the request was successful
    return ShoeSchema().dump(shoe), 201
    