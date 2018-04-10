
import os
from tests import WikiBaseTestCase
from wiki.core import Page

class TestWiki(WikiBaseTestCase):

    dir_path = os.path.dirname(os.path.realpath(__package__))

    page = Page(dir_path+'/content/test')

    def test_search(self):
        term = "interesting"
        matched = self.wiki.search(term)

        print matched # --> []

        # page = matched[0]
        # assert page.title == "Main"