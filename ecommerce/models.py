from ecommerce import db


"""
public class Product {
 public int ProductID { get; set; }
 public string Name { get; set; }
 public string Description { get; set; }
 public decimal Price { get; set; }
 public string Category { get; set; }
}
"""
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    image_flie = db.Column(db.String(20), nullable=False, default='default.jpg')
