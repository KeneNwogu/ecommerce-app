from flask import render_template, request, url_for, redirect, flash, get_flashed_messages, session
from ecommerce import app
from ecommerce.models import Product
from ecommerce.forms import CartForm, OrderForm, Cart, CartLine

page_size = 3
def get_categories():
    products_ = Product.query.all()
    categories = []
    for product in products_:
        if product.category not in categories:
            categories.append(product.category)
    return categories

def get_cart():
    obj = Cart()
    # cart_ = { "line_collection": obj.line_collection, "compute_total_value": obj.compute_total_value, "add_item": obj.add_item }
    # session['cart'] = cart_
    # cart = session['cart']
    return obj


@app.route("/")
@app.route("/products")
def products():
    form = CartForm()
    cart = get_cart()
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=page_size)
    categories = get_categories()
    return render_template('list.html', cart=cart, products=products, categories=categories, form=form)


@app.route("/<category>")
def category(category):
    form = CartForm()  
    cart = get_cart()
    page = request.args.get('page', 1, type=int)
    category_products = Product.query.filter_by(category=category).paginate(page=page, per_page=page_size)
    products_ = Product.query.all()

    categories = []
    for product in products_:
        if product.category not in categories:
            categories.append(product.category)

    return render_template("list.html", category_products=category_products, categories=categories, form=form, cart=cart)


@app.route("/cart/index", methods=['GET'])
def index():
    cart = get_cart()
    form = CartForm()
    return_url = "/"
    return render_template("cart.html", return_url=return_url, form=form, cart=cart) 

@app.route("/cart", methods=['GET', 'POST'])
def add_to_cart():
    form = CartForm() 
    cart = get_cart()
    return_url = request.referrer # gets previous page
    if form.validate_on_submit():
        # get product
        product = Product.query.filter_by(id = form.id.data).first()
        line = CartLine(product, 0)
        cart.add_item(line, 1)
    return render_template("cart.html", cart=cart, return_url=return_url, title="Your Cart- SPORTS STORE", form=form)

@app.route("/cart/remove", methods=['GET', 'POST'])
def remove_from_cart():
    form = CartForm()
    cart = get_cart()
    return_url = request.referrer
    if form.validate_on_submit():
        product = Product.query.filter_by(id = form.id.data).first()
        cart.remove_line(product)
    return redirect(url_for('index'))

@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    form = OrderForm()
    cart = get_cart()
    categories = get_categories()
    return render_template('checkout.html', form=form, categories=categories, cart=cart)

