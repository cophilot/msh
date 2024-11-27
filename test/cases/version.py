from msh import MSH
from test_case import TestCase


class VersionTestCase(TestCase):
    def __init__(self):
        super().__init__("version")

    def run(self):
        MSH.run_suc("version")
