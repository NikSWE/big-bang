# Created by Nikhil Anand <nick.muj.programmer@gmail.com>
#
# This module provides functions to `print`
# status messages on the `console/terminal`

import subprocess

# print message color constants
RESET = '\033[0m'  # Reset Prompt
RED = '\033[0;31m'  # Error
GREEN = '\033[0;32m'  # Success
YELLOW = '\033[0;33m'  # Processing
BLUE = '\033[0;34m'  # New Stage


# print success message
def print_green(message):
    subprocess.call(["echo", "{}{}{}".format(GREEN, message, RESET)])


# print error message
def print_red(message):
    subprocess.call(["echo", "{}{}{}".format(RED, message, RESET)])


# print in-progress message
def print_yellow(message):
    subprocess.call(["echo", "{}{}{}".format(YELLOW, message, RESET)])


# print current-stage message
def print_blue(message):
    subprocess.call(["echo", "{}{}{}".format(BLUE, message, RESET)])
