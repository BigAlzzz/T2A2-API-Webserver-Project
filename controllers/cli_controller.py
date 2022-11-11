from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.user_shoe import Shoe, User
from models.condition import Condition
from models.size import Size
from models.user import UserSchema



db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Cleese',
            email='someone@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    conditions = [
        Condition(
            name = "New"
        )
    
    ]

    db.session.add_all(conditions)
    db.session.commit()

    sizes = [
        Size(
            size = 9,
            gender = "male",
        )
    ]
    db.session.add_all(sizes)
    db.session.commit()

    shoes = [
        Shoe(
            brand = "Nike",
            name = "Air Jordan 1",
            description = "Bred 2013",
            release_date = date(2013,12,28),
            condition_id = 1,
            size_id = 1
        ),
        Shoe(
            brand = "Nike",
            name = "Air Jordan 2",
            description = "Cookie 2013",
            release_date = date(2014,12,28),
            condition_id = 1,
            size_id = 1
        )
        
    ]
    db.session.add_all(shoes)

    airforce = users[0]
    airforce.shoes.append(shoes[0])


    
    db.session.commit()

    print('Tables seeded')