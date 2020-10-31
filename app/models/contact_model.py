from app import db
from app.models.base_model import BaseModel


class ContactModel(BaseModel):

    __tablename__ = 'user_contact'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(10), nullable=True)
    subject = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(), nullable=False)

    def __init__(self, name, email, phone, subject, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.subject = subject
        self.message = message

    def __repr__(self):
        return f'<User {self.name} message #{self.id}>'
