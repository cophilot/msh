from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal

class $$name.p$$TestCase(TestCase):
    def __init__(self):
        super().__init__("$$name.l$$")

    def run(self):
        MSH.run_suc("$$name.l$$")
