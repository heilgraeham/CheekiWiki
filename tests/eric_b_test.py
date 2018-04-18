# -*- coding: utf-8 -*-
from . import WikiBaseTestCase
import pyrebase
import json
import random, string


class TestFirebase (WikiBaseTestCase):

    def test_authenticate_user(self):
        firebase = pyrebase.initialize_app(json.load(open('user/cheekiwiki-firebase-admin.json')))
        auth = firebase.auth()
        result = auth.sign_in_with_email_and_password("test@gmail.com", "123456")
        assert result.get("idToken") is not None

    def test_create_user(self):
        firebase = pyrebase.initialize_app(json.load(open('user/cheekiwiki-firebase-admin.json')))
        auth = firebase.auth()
        random_email = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        result = auth.create_user_with_email_and_password(random_email + "@gmail.com", "123456")
        assert result.get("idToken") is not None