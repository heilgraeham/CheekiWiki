# -*- coding: utf-8 -*-
import os
from random import random
from wiki.web.user import UserManager
from . import WikiBaseTestCase

class TestUser (WikiBaseTestCase):

    dir_path = os.path.dirname(os.path.realpath(__package__))
    user = UserManager(dir_path + '/user/')

    def test_get_user(self):
        assert 'name' == self.user.get_user('name').name

    def test_check_password(self):
        assert self.user.get_user('name').check_password('1234') is True
        assert self.user.get_user('name').check_password('4321') is False

    def test_add_user(self):
        assert self.user.add_user('name', '5678') is False

    def test_update(self):
        rand = random()
        user = self.user.get_user('test')
        data = {u'active': False, u'authentication_method': u'cleartext', u'password': str(rand), u'authenticated': True, u'roles': ['unit test']}
        self.user.update(user.name, data)
        assert self.user.get_user(user.name).data == data

