from msh import MSH
from test_case import TestCase


class RunTestCase(TestCase):
    def __init__(self):
        super().__init__("run")

    def run(self):

        # run|r <script> [flags] - Run a script
        #       script - The name of the script to run
        #       Flags:
        #           -args|-a - Provide arguments for the script
        #           -extend|-x - Print the scripts commands while running
        #           -clear-log|-cl - Clear the command and run logs before running the script

        MSH.run_fail("run")

        MSH.run_suc("new test-script -say-hello")

        o = MSH.run_suc("run test-script")
        o.has_line("Hello from test-script!")

        MSH.HOME.add_file(".run_history.log").check().has_line(
            "/test-script", can_be_substring=True
        ).has_line("Hello from test-script!", can_be_substring=True)
        MSH.HOME.add_file(".cmd_history.log").check().has_line(
            "/test-script", can_be_substring=True
        )
