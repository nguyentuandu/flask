from sqlalchemy import Column, Integer,String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import db,app


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
if __name__ == '__main__':
    with app.app_context():
        c4 = Product(name='Samsung galaxy s5',price=10000000,category_id=1)
        c5 = Product(name='Oppo',price=20000000,category_id=2)
        c6 = Product(name='Dell insprion 3000',price=30000000,category_id=3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)
        db.session.commit()

        #db.create_all()