from datetime import datetime

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from market import app, db
from market.forms import AddingForm, LoginForm, RegisterForm, SubmitOrderForm
from market.models import (BabyProducts, Beverages, Categories, FoodProducts,
                           OrderDetails, Orders, PetProducts, Snacks, User)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # Create a user
        user_to_create = User(name=form.username.data,
                              email=form.email_address.data,
                              phone=form.phone.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)

        # Get created user
        created_user = User.query.order_by(User.id.desc()).first()

        flash(f"Вітаємо, акаунт успішно створено! Тепер, ви авторизовані як: {user_to_create.name}!",
              category='success')

        # Add new order to DB
        new_order = Orders(user_id=created_user.id)
        db.session.add(new_order)
        db.session.commit()

        order_id = new_order.order_id

        # Update new order
        order_details = OrderDetails(order_id=order_id)
        db.session.add(order_details)
        db.session.commit()

        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'УПС! Сталась помилка при створені користувача: {err_msg}',
                  category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(name=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Успіх! Ви авторизовані як: {attempted_user.name}',
                  category='success')
            return redirect(url_for('home_page'))
        else:
            flash('УПС! Сталась помилка... Спробуйте ще раз!', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Ви більше не авторизовані!", category='info')
    return redirect(url_for("home_page"))


@app.route('/food', methods=['GET', 'POST'])
@login_required
def food_page():
    adding_form = AddingForm()
    if request.method == "POST":
        # Get chosen item from user
        added_item = request.form.get('added_item')
        added_item_object = FoodProducts.query.filter_by(name=added_item).first()
        if added_item_object:
            current_user_id = current_user.id
            order_detail = OrderDetails.query.filter_by(order_id=current_user_id).first()
            # Update an existing ID field
            order_detail.product_id = added_item_object.id
            # Update the price to pay
            if order_detail.price is None:
                order_detail.price = 0
            order_detail.price += added_item_object.price
            db.session.commit()

            flash(f"Товар '{added_item_object.name}' додано до кошика!", category='success')

            if order_detail and order_detail.all_fields_have_values():
                flash("Ваш кошик повний! Хочете зробити замовлення?", category='info')
                return redirect(url_for('cart_page'))
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        items = FoodProducts.query.all()
        category_id = FoodProducts.category_id
        category = Categories.query.filter_by(id=category_id).first()
        return render_template('food.html', items=items, category=category,
                               adding_form=adding_form)


@app.route('/beverages', methods=['GET', 'POST'])
@login_required
def beverages_page():
    adding_form = AddingForm()
    if request.method == "POST":
        # Get chosen item from user
        added_item = request.form.get('added_item')
        added_item_object = Beverages.query.filter_by(name=added_item).first()
        if added_item_object:
            current_user_id = current_user.id
            order_detail = OrderDetails.query.filter_by(order_id=current_user_id).first()
            # Update an existing ID field
            order_detail.beverage_id = added_item_object.id
            # Update the price to pay
            if order_detail.price is None:
                order_detail.price = 0
            order_detail.price += added_item_object.price
            db.session.commit()

            flash(f"Товар '{added_item_object.name}' додано до кошика!", category='success')

            if order_detail and order_detail.all_fields_have_values():
                flash("Ваш кошик повний! Хочете зробити замовлення?", category='info')
                return redirect(url_for('cart_page'))
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        items = Beverages.query.all()
        category_id = Beverages.category_id
        category = Categories.query.filter_by(id=category_id).first()
        return render_template('beverages.html', items=items, category=category,
                               adding_form=adding_form)


@app.route('/baby_products', methods=['GET', 'POST'])
@login_required
def baby_products_page():
    adding_form = AddingForm()
    if request.method == "POST":
        # Get chosen item from user
        added_item = request.form.get('added_item')
        added_item_object = BabyProducts.query.filter_by(name=added_item).first()
        if added_item_object:
            current_user_id = current_user.id
            order_detail = OrderDetails.query.filter_by(order_id=current_user_id).first()
            # Update an existing ID field
            order_detail.baby_food_id = added_item_object.id
            # Update the price to pay
            if order_detail.price is None:
                order_detail.price = 0
            order_detail.price += added_item_object.price
            db.session.commit()

            flash(f"Товар '{added_item_object.name}' додано до кошика!", category='success')

            if order_detail and order_detail.all_fields_have_values():
                flash("Ваш кошик повний! Хочете зробити замовлення?", category='info')
                return redirect(url_for('cart_page'))
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        items = BabyProducts.query.all()
        category_id = BabyProducts.category_id
        category = Categories.query.filter_by(id=category_id).first()
        return render_template('baby_products.html', items=items, category=category,
                               adding_form=adding_form)


@app.route('/pet_products', methods=['GET', 'POST'])
@login_required
def pet_products_page():
    adding_form = AddingForm()
    if request.method == "POST":
        # Get chosen item from user
        added_item = request.form.get('added_item')
        added_item_object = PetProducts.query.filter_by(name=added_item).first()
        if added_item_object:
            order_detail = OrderDetails.query.filter_by(order_id=current_user.id).first()
            # Update an existing ID field
            order_detail.pet_id = added_item_object.id
            # Update the price to pay
            if order_detail.price is None:
                order_detail.price = 0
            order_detail.price += added_item_object.price
            db.session.commit()

            flash(f"Товар '{added_item_object.name}' додано до кошика!", category='success')

            if order_detail and order_detail.all_fields_have_values():
                flash("Ваш кошик повний! Хочете зробити замовлення?", category='info')
                return redirect(url_for('cart_page'))
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        items = PetProducts.query.all()
        category_id = PetProducts.category_id
        category = Categories.query.filter_by(id=category_id).first()
        return render_template('pet_products.html', items=items, category=category,
                               adding_form=adding_form)


@app.route('/snacks', methods=['GET', 'POST'])
@login_required
def snacks_page():
    adding_form = AddingForm()
    if request.method == "POST":
        # Get chosen item from user
        added_item = request.form.get('added_item')
        added_item_object = Snacks.query.filter_by(name=added_item).first()
        if added_item_object:
            order_detail = OrderDetails.query.filter_by(order_id=current_user.id).first()
            # Update an existing ID field
            order_detail.snack_id = added_item_object.id
            # Update the price to pay
            if order_detail.price is None:
                order_detail.price = 0
            order_detail.price += added_item_object.price
            db.session.commit()

            flash(f"Товар '{added_item_object.name}' додано до кошика!", category='success')

            if order_detail and order_detail.all_fields_have_values():
                flash("Ваш кошик повний! Хочете зробити замовлення?", category='info')
                return redirect(url_for('cart_page'))
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        items = Snacks.query.all()
        category_id = Snacks.category_id
        category = Categories.query.filter_by(id=category_id).first()
        return render_template('snacks.html', items=items, category=category,
                               adding_form=adding_form)


@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart_page():
    submission_form = SubmitOrderForm()
    is_ordered = Orders.query.filter_by(user_id=current_user.id).first().order_date is not None
    if request.method == "POST":
        # Update an existing order's date
        order = Orders.query.filter_by(user_id=current_user.id).first()
        order.order_date = datetime.now().strftime('%Y-%m-%d')
        db.session.commit()

        flash("Замовлення успішно записано, та скоро буде виконано!", category='success')
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        # Get all IDs of chosen items
        order_details = OrderDetails.query.filter_by(order_id=current_user.id).first()
        product_id = order_details.product_id
        beverage_id = order_details.beverage_id
        baby_food_id = order_details.baby_food_id
        pet_id = order_details.pet_id
        snack_id = order_details.snack_id
        total_price = order_details.price

        # Get all chosen items
        product = FoodProducts.query.filter_by(id=product_id).first()
        beverage = Beverages.query.filter_by(id=beverage_id).first()
        baby_food = BabyProducts.query.filter_by(id=baby_food_id).first()
        pet_food = PetProducts.query.filter_by(id=pet_id).first()
        snack = Snacks.query.filter_by(id=snack_id).first()

        items = [product, beverage, baby_food, pet_food, snack]

        return render_template('cart.html', items=items, total_price=total_price,
                               submission_form=submission_form, is_ordered=is_ordered)
