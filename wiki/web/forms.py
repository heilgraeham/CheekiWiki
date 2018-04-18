"""
    Forms
    ~~~~~
"""
from flask_wtf import Form
from wtforms import BooleanField
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError
from wiki.core import clean_url
from wiki.web import current_wiki
import pyrebase
from user import UserManager
from flask import current_app
import json

class URLForm(Form):
    url = TextField('', [InputRequired()])

    def validate_url(form, field):
        if current_wiki.exists(field.data):
            raise ValidationError('The URL "%s" exists already.' % field.data)

    def clean_url(self, url):
        return clean_url(url)


class SearchForm(Form):
    term = TextField('', [InputRequired()])
    ignore_case = BooleanField(
        description='Ignore Case',
        # FIXME: default is not correctly populated
        default=True)


class EditorForm(Form):
    title = TextField('', [InputRequired()])
    body = TextAreaField('', [InputRequired()])
    tags = TextField('')


class LoginForm(Form):
    name = TextField('', [InputRequired()])
    password = PasswordField('', [InputRequired()])

    firebase = pyrebase.initialize_app(json.load(open('user/cheekiwiki-firebase-admin.json')))

    auth = firebase.auth()

    def sign_in(self, user, password):
        response = self.auth.sign_in_with_email_and_password(user, password)
        if response.get("idToken"):
            self.retain_user(user, password)
            return

    def create_user(self, user, password):
        response = self.auth.create_user_with_email_and_password(user, password)
        if response.get("idToken"):
            self.retain_user(user, password)
            return

    def retain_user(self, user, password):
        UserManager(current_app.config['USER_DIR']).add_user(user, password, True, [], None)
