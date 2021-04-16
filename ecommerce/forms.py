from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CartForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    return_url = StringField('return_url', validators=[DataRequired()])
    submit = SubmitField('Add To Cart')

class OrderForm(FlaskForm):       
    name = StringField('Name', validators=[DataRequired(message="Please enter a name")])
    line_1 = StringField('Line 1', validators=[DataRequired(message="Please enter first address line")])
    line_2 = StringField('Line 2')
    line_3 = StringField('Line 3')
    city = StringField('City', validators=[DataRequired(message='Please enter a city name')])
    state = StringField('State', validators=[DataRequired(message='Please enter a state name')])
    zip_ = StringField('Zip')
    country = StringField('Country', validators=[DataRequired(message='Please enter a country name')])
    gift_wrap = BooleanField()
    submit = SubmitField('Complete Order')

class Cart():
    line_collection = []

    def add_item(self, line, quantity):
        names = [l.product.name for l in self.line_collection]
        if line.product.name not in names:
            line.quantity += quantity
            self.line_collection.append(line)
        else:
            index = names.index(line.product.name)
            self.line_collection[index].quantity += quantity


    def remove_line(self, product):
        for line in self.line_collection:
            if line.product.name == product.name:
                self.line_collection.remove(line)

    def compute_total_value(self):
        return sum([line.product.price * line.quantity for line in self.line_collection])

    def compute_quantity_sum(self):
        return sum([line.quantity for line in self.line_collection])
    
    def clear(self):
        self.line_collection.clear()
    
    def lines(self):
        return self.line_collection

class CartLine():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
