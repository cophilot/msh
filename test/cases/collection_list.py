from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class CollectionListTestCase(TestCase):
    def __init__(self):
        super().__init__("collection-list")

    def run(self):

        #  collection|c list|ls - List all collections

        o = MSH.run_suc("collection list")
        assert_equal(1, o.length())

        MSH.run_suc("collection new test")
        MSH.run_suc("collection new test1")
        MSH.run_suc("collection new test2")

        o = MSH.run_suc("collection list")
        o.has_line("test")
        o.has_line("test1")
        o.has_line("test2")
