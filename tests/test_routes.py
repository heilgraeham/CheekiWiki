import os
from wiki.web.routes import checktags
from . import WikiBaseTestCase

class TestRoutes(WikiBaseTestCase):

    def test_duplicate_tags(self):
        assert checktags(["home", "home"]) == 1
        print "duplicate tags found"

        assert checktags(["home", "index", "wiki", "home"]) == 1
        print "duplicate tags found"

        assert checktags(["wiki", "software", "engineering"]) == 0
        print "no duplicate tags found"




