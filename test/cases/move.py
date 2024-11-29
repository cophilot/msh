from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class MoveTestCase(TestCase):
    def __init__(self):
        super().__init__("move")

    def run(self):

        # move|mv <script> <dest-collection> - Move a script to a different collection
        #   script - The name of the script to move
        #   dest-collection - The name of the collection to move the script to

        MSH.run_suc("new test-script")
        MSH.run_suc("collection new test-collection")

        MSH.run_fail("move")
        MSH.run_fail("move test-script")
        MSH.run_fail("move test-script test-collection-not-exist")
        MSH.run_fail("move test-script-not-exist test-collection")
        MSH.run_suc("move test-script test-collection")

        MSH.HOME.add_dir("test-collection").add_file("test-script").check()
        MSH.HOME.cd("scripts").add_file("test-script").check_not_exists()
