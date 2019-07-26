# Created by Nikhil Anand <nick.muj.programmer@gmail.com>
#
# Currently the script only supports `Mac OSX`
#
# TODO: Add support for following platforms
# - `Linux`
# - `Windows`
#
# This script downloads all the dependencies which are needed
# to setup the system. It also initializes the `src/main.py`

# print message color constants
RESET='\033[0m'     # Reset Prompt
RED='\033[0;31m'    # Error
GREEN='\033[0;32m'  # Success
YELLOW='\033[0;33m' # Processing
BLUE='\033[0;34m'   # New Stage

# print current stage [1]
echo "${BLUE}1] setting up the environment${RESET}"

# downloading `Xcode command line tools`
xcode-select --install

# downloading `homebrew`
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# updating `homebrew`
brew update

# downloading `python 3.x.x`
brew install python

# print stage completed [1]
echo "${GREEN}successfully installed dependencies${RESET}"

# print current stage [2]
echo "${BLUE}2] setting up the workstation${RESET}"

# invoke `main.py` in src directory
time python3 -B src/main.py
