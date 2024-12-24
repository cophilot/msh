from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class EditTestCase(TestCase):
    def __init__(self):
        super().__init__("edit")

    def run(self):

        # edit|e [script-name] - Open a specified or all scripts in the editor
        #   script-name - If provided, the script with the specified name will be opened in the editor

        MSH.run_suc("edit").has_line(MSH.HOME.get_abs_path())

        MSH.run_fail("edit test-script")

        MSH.run_suc("new test-script")
        MSH.run_suc("edit test-script").has_line(
            MSH.HOME.get_abs_path() + "/scripts/test-script"
        )
