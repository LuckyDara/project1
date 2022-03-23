from random import choices
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    proptitle= StringField('Property Title', validators=[DataRequired()])
    desc=TextAreaField('Description', validators=[DataRequired()])
    num_of_bedrooms=StringField('No. of Rooms', validators=[DataRequired()])
    num_of_bathrooms=StringField('No. of Bathrooms', validators=[DataRequired()])
    price=StringField('Price', validators=[DataRequired()])
    proptype= SelectField('Property Type', choices=[('House', 'House'),('Apartment', 'Apartment')], validators=[DataRequired()])
    location=StringField('Location', validators=[DataRequired()])
    photo=FileField('Photo', validators=[FileRequired(), FileAllowed(['png','jpg','Image files only'])])