from app.Models import Category, Product


def get_categories():
    return Category.query.all()


def get_products(kw):
    products = Product.query
    return products.all()
