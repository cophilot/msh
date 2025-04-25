import datetime
from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class ListTestCase(TestCase):
    def __init__(self):
        super().__init__("list")

    def run(self):

        # list|ls [tag] [flags] - List all available commands
        #   tag - If provided, only scripts with the specified tag will be listed
        #   Flags:
        #       -collection|-c - Show the collection of the scripts
        #       -group|-g - Group the scripts by collection
        #       -simple|-s - Print the list in a simple format
        #       -time|-t - Print the time tag of the script

        MSH.run_suc("collection new my-collection")
        MSH.run_suc("collection new my-collection2")

        MSH.run_suc("new test-script")
        MSH.run_suc("new test-script2 my-collection")
        MSH.run_suc("new test-script3 my-collection2")

        MSH.run_suc("list").has_lines(
            [
                "SCRIPT DESCRIPTION",
                "test-script This is the test-script script [TAGS]",
                "test-script2 This is the test-script2 script [TAGS]",
                "test-script3 This is the test-script3 script [TAGS]",
            ],
            ignore_whitespaces=True,
        )

        MSH.run_suc("list -collection").has_lines(
            [
                "SCRIPT COLLECTION DESCRIPTION",
                "test-script scripts This is the test-script script [TAGS]",
                "test-script2 my-collection This is the test-script2 script [TAGS]",
                "test-script3 my-collection2 This is the test-script3 script [TAGS]",
            ],
            ignore_whitespaces=True,
        )

        curr_date = datetime.datetime.now().strftime("%Y-%m-%d")

        MSH.run_suc("list -time").has_lines(
            [
                "SCRIPT TIME-TAG DESCRIPTION",
                f"test-script {curr_date} This is the test-script script [TAGS]",
                f"test-script2 {curr_date} This is the test-script2 script [TAGS]",
                f"test-script3 {curr_date} This is the test-script3 script [TAGS]",
            ],
            ignore_whitespaces=True,
        )

        MSH.run_suc("list -t -c").has_lines(
            [
                "SCRIPT COLLECTION TIME-TAG DESCRIPTION",
                f"test-script scripts {curr_date} This is the test-script script [TAGS]",
                f"test-script2 my-collection {curr_date} This is the test-script2 script [TAGS]",
                f"test-script3 my-collection2 {curr_date} This is the test-script3 script [TAGS]",
            ],
            ignore_whitespaces=True,
        )

        MSH.HOME.cd("scripts").add_file(
            "web-test-script",
            content="#??This is the web-test-script script\n#&&web,test",
        ).make()

        MSH.HOME.cd("scripts").add_file(
            "bash-test-script",
            content="#??This is the bash-test-script script\n#&&bash,test",
        ).make()

        l = MSH.run_suc("list web")
        l.has_line(
            "web-test-script This is the web-test-script script [web,test]",
            ignore_whitespaces=True,
        )
        l.has_line(
            "bash-test-script This is the bash-test-script script [bash,test]",
            ignore_whitespaces=True,
            revert=True,
        )

        l = MSH.run_suc("list bash")
        l.has_line(
            "web-test-script This is the web-test-script script [web,test]",
            ignore_whitespaces=True,
            revert=True,
        )
        l.has_line(
            "bash-test-script This is the bash-test-script script [bash,test]",
            ignore_whitespaces=True,
        )

        l = MSH.run_suc("list test")
        l.has_line(
            "web-test-script This is the web-test-script script [web,test]",
            ignore_whitespaces=True,
        )
        l.has_line(
            "bash-test-script This is the bash-test-script script [bash,test]",
            ignore_whitespaces=True,
        )
