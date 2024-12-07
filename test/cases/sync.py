import os
from msh import MSH
from test_case import TestCase
from my_assertion import assert_true, assert_false, assert_equal


class SyncTestCase(TestCase):
    def __init__(self):
        super().__init__("sync")

    def run(self):

        # sync|s [collection-name] [flags] - Synchronize all or one collections
        #    collection-name - The name of the collection to synchronize
        #    Flags:
        #        -u|-up - Push changes to the remote repository
        #        -d|-detached - Synchronize the collection in detached mode

        MSH.run_suc(
            "collection clone https://github.com/cophilot/msh-test-collection.git mtc"
        )
        os.popen(
            f"cd {MSH.HOME.name}/mtc && git checkout 1ef4593f96c883bb4ed6529a1c2c43d6b45f11e2"
        )
        MSH.HOME.add_dir("mtc").add_file("msh-test-script").check_not_exists()

        MSH.run_suc("sync")
        MSH.HOME.add_dir("mtc").add_file("msh-test-script").check()
