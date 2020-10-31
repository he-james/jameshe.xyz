from flask_wtf import FlaskForm
from wtforms import StringField, FormField
from wtforms.validators import DataRequired, Email
from app.forms.telephone_form import TelephoneForm


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Name is required.")])
    email = StringField('Email Address', validators=[Email(), DataRequired('Email is required.')])
    phone = FormField(TelephoneForm, 'Phone Number')
    subject = StringField('Subject', validators=[DataRequired("Subject is required.")])
    message = StringField('Message', validators=[DataRequired("Message is required.")])
