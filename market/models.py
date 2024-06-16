from market import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))


class FoodProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2))
    image_url = db.Column(db.String(255))


class Beverages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2))
    image_url = db.Column(db.String(255))


class BabyProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2))
    image_url = db.Column(db.String(255))


class PetProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2))
    image_url = db.Column(db.String(255))


class Snacks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    price = db.Column(db.DECIMAL(10, 2))
    image_url = db.Column(db.String(255))


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_date = db.Column(db.Date)
    customer = db.relationship('User', backref='orders')


class OrderDetails(db.Model):
    order_detail_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('food_products.id'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverages.id'))
    baby_food_id = db.Column(db.Integer, db.ForeignKey('baby_products.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet_products.id'))
    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.id'))
    price = db.Column(db.DECIMAL(10, 2))

    def all_fields_have_values(self):
        for column in self.__table__.columns:
            if getattr(self, column.name) is None or getattr(self, column.name) == '':
                return False
        return True
