from msh import MSH
from msh_debug import MSHTestingDebugger
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class CopyTestCase(TestCase):
    def __init__(self):
        super().__init__("copy")

    def run(self):

        #  copy|cp <original-script> <new-script> - Copy a script to a new file
        #       original-script - The script to copy
        #       new-script - The name of the new script file

        MSH.run_suc("new og-script")
        MSH.run_suc("new other-script")

        MSH.run_fail("copy")
        MSH.run_fail("copy og-script")
        MSH.run_fail("copy og-script-2 new-script")
        MSH.run_fail("copy og-script other-script")

        MSH.run_suc("copy og-script new-script")
        MSH.HOME.cd("scripts").add_file("og-script").check()
        MSH.HOME.cd("scripts").add_file("new-script").check().has_line(
            "#??This is the og-script script"
        )
