from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class VersionTestCase(TestCase):
    def __init__(self):
        super().__init__("version")

    def run(self):

        # version|v [flags] - Print the version of myshell
        #    Flags:
        #        -s|-simple - Print the version in a simple format

        MSH.run_suc("version")
        o = MSH.run_suc("version -s")
        assert_equal(1, o.length())
