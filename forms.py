from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class submitForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(),
                                                   Length(min = 2, max = 20)])
    
    submitCoffee = SubmitField('Sign Up')




