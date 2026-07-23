from msh import MSH
from test_case import TestCase


class AutocompleteTestCase(TestCase):
    def __init__(self):
        super().__init__("autocomplete")

    def run(self):
        #  autocomplete <enable|disable|status|get> - Enable or disable autocomplete for the CLI (only works for bash)"
        #      enable - Enable autocomplete for the CLI"
        #      disable - Disable autocomplete for the CLI"
        #      status - Show the current status of autocomplete"
        #      get - Get autocomplete suggestions for the CLI"

        MSH.run_fail("autocomplete")
        MSH.run_fail("autocomplete test")

        MSH.HOME.add_file("_msh_dev_autocomplete.sh").check_not_exists()

        MSH.run_suc("autocomplete status").has_line("Autocomplete is disabled.")

        MSH.run_suc("autocomplete enable")
        MSH.HOME.add_file("_msh_dev_autocomplete.sh").check()

        MSH.run_suc("autocomplete status").has_line("Autocomplete is enabled.")

        MSH.run_suc("autocomplete disable")
        MSH.HOME.add_file("_msh_dev_autocomplete.sh").check_not_exists()

        MSH.run_suc("autocomplete status").has_line("Autocomplete is disabled.")

        MSH.run_suc("autocomplete get auto").has_line("autocomplete")
        MSH.run_suc("autocomplete get autocomplete en").has_line("enable")

        MSH.run_suc("new test-script")
        MSH.run_suc("autocomplete get run te").has_line("test-script")
