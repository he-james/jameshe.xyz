from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class TelephoneForm(FlaskForm):
    area_code = IntegerField('Area Code', validators=[DataRequired("Area Code is required")])
    number = IntegerField('Number', validators=[DataRequired("Phone Number is required")])
