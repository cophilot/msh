import sys
import traceback

from cases.help import HelpTestCase
from cases.version import VersionTestCase
from cases.new import NewTestCase
from cases.collection_new import CollectionNewTestCase
from msh import MSH


def get_all_test_cases():
    return [HelpTestCase(), VersionTestCase(), CollectionNewTestCase(), NewTestCase()]


def print_banner():
    print("                          __         ____")
    print("    ____ ___  __  _______/ /_  ___  / / /")
    print("   / __  __ \\/ / / / ___/ __ \\/ _ \\/ / / ")
    print("  / / / / / / /_/ (__  ) / / /  __/ / /  ")
    print(" /_/ /_/ /_/\\__, /____/_/ /_/\\___/_/_/   ")
    print("           /____/ TEST RUNNER")
    print("")


def main():
    print_banner()

    cases = get_all_test_cases()
    exp = []
    summary = []

    for case in cases:
        try:
            MSH.setup()
            print(f"Running {case.name} test...")
            case.run()
            msg = f"{case.name} passed✅"
            print(msg)
            summary.append(msg)
            MSH.cleanup()
        except AssertionError as e:
            exp.append({"case": case, "e": e})
            msg = f"{case.name} failed❌"
            print(msg)
            summary.append(msg)
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
