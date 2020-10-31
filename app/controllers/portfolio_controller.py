from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.forms.contact_form import ContactForm
from app.models.contact_model import ContactModel


portfolio = Blueprint('portfolio', __name__, url_prefix='/')


@portfolio.route('/', methods=['GET', 'POST'])
def index():
    return render_template("portfolio/index.html")


@portfolio.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        print(form)

    return render_template("portfolio/contact.html", form=form)