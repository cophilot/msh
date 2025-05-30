from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal
import datetime

class DetailsTestCase(TestCase):
    def __init__(self):
        super().__init__("details")

    def run(self):
        
        # details|d <script> - Get more information about a script
        #   script - The name of the script to get details for
        
        
        MSH.run_fail("details")

        MSH.run_fail("details test-script")

        curr_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        MSH.run_suc("new test-script")
        
        MSH.run_suc("details test-script").has_lines(
            [
                "Name: test-script",
                "Path: " + MSH.HOME.get_abs_path() + "/scripts/test-script",
                "Description: This is the test-script script",
                "Tags: [TAGS]",
                "Created: " + curr_date,
                "Last Modified: " + curr_date
            ],
            ignore_whitespaces=True,
            can_be_substring=True
        )
