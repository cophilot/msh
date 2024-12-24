from msh import MSH
from test_case import TestCase


class HelpTestCase(TestCase):
    def __init__(self):
        super().__init__("help")

    def run(self):

        #  help|h - Get help for myshell

        MSH.run_suc("help")
