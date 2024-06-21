from __future__ import annotations

import sys


def main():  # needed for console script
    print("Welcome to time-functions!")
    print("--------------------------")
    print("Commands:")
    print("    list <time_functions.cli.list>")
    print("    stress <time_functions.cli.stress>")


if __name__ == "__main__":
    sys.exit(main())
