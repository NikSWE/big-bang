from simple_colors import *  # pylint: disable=unused-wildcard-import


def success(str):
    print(green(str))  # pylint: disable=undefined-variable


def error(str):
    print(red(str))  # pylint: disable=undefined-variable


def warning(str):
    print(yellow(str))  # pylint: disable=undefined-variable