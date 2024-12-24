import sys
import traceback

from cases.help import HelpTestCase
from cases.version import VersionTestCase
from cases.new import NewTestCase
from cases.move import MoveTestCase
from cases.remove import RemoveTestCase
from cases.restore import RestoreTestCase
from cases.list import ListTestCase
from cases.print import PrintTestCase
from cases.edit import EditTestCase
from cases.manual import ManualTestCase
from cases.collection_new import CollectionNewTestCase
from cases.collection_list import CollectionListTestCase
from cases.collection_clone import CollectionCloneTestCase
from msh import MSH

FILTER = ""


def get_all_test_cases():
    print("here2")
    return [
        HelpTestCase(),
        VersionTestCase(),
        CollectionNewTestCase(),
        CollectionListTestCase(),
        CollectionCloneTestCase(),
        NewTestCase(),
        ListTestCase(),
        ManualTestCase(),
        EditTestCase(),
        PrintTestCase(),
        MoveTestCase(),
        RemoveTestCase(),
        RestoreTestCase(),
    ]


def print_banner():
    print("                          __         ____")
    print("    ____ ___  __  _______/ /_  ___  / / /")
    print("   / __  __ \\/ / / / ___/ __ \\/ _ \\/ / / ")
    print("  / / / / / / /_/ (__  ) / / /  __/ / /  ")
    print(" /_/ /_/ /_/\\__, /____/_/ /_/\\___/_/_/   ")
    print("           /____/ TEST RUNNER")
    print("")


def filter_cases(cases):
    return cases


def main():
    print_banner()

    cases = filter_cases(get_all_test_cases())
    exp = []
    summary = []
    print("here")
    for case in cases:
        try:
            MSH.setup()
            print(f"Running {case.name} test...")
            case.run()
            msg = f"{case.name} passed✅"
            print(msg)
            summary.append(msg)
        except AssertionError as e:
            exp.append({"case": case, "e": e})
            msg = f"{case.name} failed❌"
            print(msg)
            summary.append(msg)
        finally:
            MSH.cleanup()
    print_errors_and_exit(exp, summary)


def print_errors_and_exit(exp, summary):
    print()

    if len(exp) == 0:
        print("All tests passed✅✅✅")
        print_summary(summary)
        sys.exit(0)

    print(f"{len(exp)} tests failed❌❌❌")
    for ex in exp:
        e = ex["e"]
        print()
        print(f"  {e.__class__.__name__} in {ex["case"].name} test:")
        traceback.print_tb(e.__traceback__)
        print(f"  {e}")

    print_summary(summary)
    sys.exit(1)


def print_summary(summary):
    print()
    print("Summary:")
    for msg in summary:
        print(msg)


if __name__ == "__main__":
    main()
