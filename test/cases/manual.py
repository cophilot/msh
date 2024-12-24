from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class ManualTestCase(TestCase):
    def __init__(self):
        super().__init__("manual")

    def run(self):

        # manual|m <script> - Get the manual for the script
        #   script - The name of the script to get the manual for

        MSH.run_fail("manual")

        MSH.run_suc("new test-script -man")
        MSH.run_suc("manual test-script").has_line(
            "This is the manual for the test-script command..."
        )
