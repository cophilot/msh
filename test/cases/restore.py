from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class RestoreTestCase(TestCase):
    def __init__(self):
        super().__init__("restore")

    def run(self):

        # restore <script> [collection-name] - Restore a script from the trash
        #     script - The name of the script to restore
        #     collection-name - The name of the collection to restore the script to

        MSH.run_suc("collection new test-collection")
        MSH.run_suc("new test-script")
        MSH.run_suc("remove test-script")

        MSH.run_fail("restore")
        MSH.run_fail("restore not-existing")

        MSH.run_suc("restore test-script")

        MSH.HOME.add_dir(".trash").add_file("test-script").check_not_exists()
        MSH.HOME.cd("scripts").add_file("test-script").check()

        MSH.run_suc("remove test-script")
        MSH.HOME.add_dir(".trash").add_file("test-script").check()

        MSH.run_suc("restore test-script test-collection")
        MSH.HOME.cd("scripts").add_file("test-script").check_not_exists()
        MSH.HOME.add_dir("test-collection").add_file("test-script").check()
