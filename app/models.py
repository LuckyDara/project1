from cgi import print_exception
from . import db

class Property(db.Model):
    __tablename__ = 'properties'
     
    id= db.Column(db.Integer, primary_key=True)
    proptitle=db.Column(db.String(100))
    desc=db.Column(db.Text)
    num_of_rooms=db.Column(db.Integer)
    num_of_bathrooms=db.Column(db.Integer)
    price=db.Column(db.Integer)
    proptype= db.Column(db.String(10))
    location=db.Column(db.String(100))
    photo=db.Column(db.String(255))
     
    def __init__(self, title, desc, num_of_bedrooms, num_of_bathrooms, price, location, type, photo):
        self.proptitle = title
        self.num_of_rooms = num_of_bedrooms
        self.num_of_bathrooms = num_of_bathrooms
        self.location = location
        self.price = price
        self.desc = desc
        self.proptype = type
        self.photo = photo
    
    def __repr__(self):
        return '<Title %r>' % (self.proptitle)