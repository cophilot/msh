from msh import MSH
from test_case import TestCase
from my_assertion import assert_true


class NewTestCase(TestCase):
    def __init__(self):
        super().__init__("new")

    def run(self):

        # new|n <new-script> [collection-name] [flags]- Create a new script
        #   script-name - The name of the script to create
        #   collection-name - The name of the collection to add the script to. The default collection can be set in the config
        #   Flags:
        #       -edit|-e - Open the script in the editor after creation
        #       -man|-m - Add a manual to the script

        MSH.run_fail("new")

        MSH.run_suc("new test-script")
        MSH.HOME.cd("scripts").add_file("test-script").check().has_line("#!/bin/bash")
        MSH.HOME.cd("scripts").add_file("test-script").check().has_line(
            "#??This is the test-script script"
        )
        MSH.HOME.cd("scripts").add_file("test-script").check().has_line("#&&TAGS")

        MSH.run_suc("new test-script-with-man -man")
        MSH.HOME.cd("scripts").add_file("test-script-with-man").check().has_line(
            "###This is the manual for the test-script-with-man command..."
        )

        MSH.run_fail("new test-script")

        MSH.run_suc("collection new my-collection")
        MSH.run_suc("new test-script my-collection")
        MSH.HOME.add_dir("my-collection").add_file("test-script").check()
        MSH.run_fail("new test-script my-collection")

        o = MSH.run_suc("new test-script-edit my-collection -edit")
        o.has_line(f"{MSH.HOME.get_abs_path()}/my-collection/test-script-edit")
