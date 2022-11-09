from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.shoe import Shoe
from models.user import User



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

    shoes = [
        Shoe(
            brand = "Nike",
            name = "Air Jordan 1",
            description = "Bred 2013",
            release_date = date(2013,12,28),
            condition_id = "1",
            size_id = "2"
        )
    ]

    db.session.add_all(shoes)
    db.session.commit()

    print('Tables seeded')