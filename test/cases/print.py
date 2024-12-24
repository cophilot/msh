from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class PrintTestCase(TestCase):
    def __init__(self):
        super().__init__("print")

    def run(self):

        # print|p <script-name> [flags] - Print the contents of a script
        #   script-name - The name of the script to print
        #   Flags:
        #       -run|-r - Run the script after printing

        MSH.run_fail("print")

        MSH.run_fail("print test-script")

        MSH.run_suc("new test-script")
        MSH.run_suc("print test-script").has_lines(
            [
                "File: " + MSH.HOME.get_abs_path() + "/scripts/test-script",
                "#!/bin/bash",
                "#??This is the test-script script",
                "#&&TAGS",
            ]
        )
