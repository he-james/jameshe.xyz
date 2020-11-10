from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.forms.contact_form import ContactForm
from app.models.contact_model import ContactModel


blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('', methods=['GET', 'POST'])
def home():
    return render_template("blog/blog-index.html")


