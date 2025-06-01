from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class CollectionCloneTestCase(TestCase):
    def __init__(self):
        super().__init__("collection-clone")

    def run(self):

        # collection|c clone|c <url> [collection-name] [flags] - Clone a collection from a git repository
        #   url - The URL of the git repository to clone
        #   collection-name - The name of the collection to create. Default is the name of the repository
        #      Flags:
        #        -print-path|-P - Print the path of the cloned collection

        MSH.run_fail("collection clone")

        MSH.run_suc(
            "collection clone https://github.com/cophilot/msh-test-collection.git"
        )
        MSH.HOME.add_dir("msh-test-collection").add_file("msh-test-script").check()
        MSH.HOME.add_dir("msh-test-collection").add_file("msh-test-script2").check()

        MSH.run_suc(
            "collection clone https://github.com/cophilot/msh-test-collection.git test-coll"
        )
        MSH.HOME.add_dir("test-coll").add_file("msh-test-script").check()
        MSH.HOME.add_dir("test-coll").add_file("msh-test-script2").check()

        path =  MSH.HOME.add_dir("test-coll2").get_abs_path()
        
        MSH.run_suc(
            "collection clone https://github.com/cophilot/msh-test-collection.git test-coll2 -print-path"
        ).has_line(path)
