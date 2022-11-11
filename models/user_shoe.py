from init import ma, db

association_table = db.Table(
    "user_shoe",
    # Base.metadata,
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True),
    db.Column("shoe_id", db.ForeignKey("shoes.id"), primary_key=True),
    
)


class Shoe(db.Model):
    __tablename__ = 'shoes'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    name = db.Column(db.String, nullable=False)
    description = db.Column( db.Text)
    release_date = db.Column(db.Date)

    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.id'), nullable=False)
    condition = db.relationship("Condition", back_populates='shoes')

    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'), nullable=False)
    size = db.relationship("Size", back_populates='shoes')

    users = db.relationship(
        "User", secondary=association_table, back_populates="shoes"
    )

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    shoes = db.relationship(
        "Shoe", secondary=association_table, back_populates="users"
    )