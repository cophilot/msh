from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class RemoveTestCase(TestCase):
    def __init__(self):
        super().__init__("remove")

    def run(self):

        # remove|rm <script> [flags] - Remove a script
        #   script - The name of the script to remove
        #   Flags:
        #       -force|-f - Remove script without storing it in the trash

        MSH.run_suc("new test-script")

        MSH.run_fail("remove")
        MSH.run_fail("remove test-script-not-exist")

        MSH.run_suc("remove test-script -force")
        MSH.HOME.add_dir(".trash").add_file("test-script").check_not_exists()

        MSH.run_suc("new test-script")
        MSH.run_suc("remove test-script")
        MSH.HOME.add_dir(".trash").add_file("test-script").check()
