from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class CollectionNewTestCase(TestCase):
    def __init__(self):
        super().__init__("collection-new")

    def run(self):

        # collection|c new|n <collection-name> - Create a new collection
        #    collection-name - The name of the collection to create

        MSH.run_fail("collection new")

        MSH.run_suc("collection new my-collection")
        MSH.HOME.add_dir("my-collection").check()

        MSH.run_suc("collection new my-collection2")
        MSH.HOME.add_dir("my-collection2").check()

        MSH.run_fail("collection new my-collection")
        MSH.run_fail("collection new my-collection2")
