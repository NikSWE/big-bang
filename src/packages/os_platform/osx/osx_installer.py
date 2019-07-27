# Created by Nikhil Anand <nick.muj.programmer@gmail.com>
#
# This script installs the software(s) mentioned
# in the configuration file at `config/osx_config.json`

import os
import json
import subprocess
import pathlib

from packages import colors


def osx_installer(config_file_path):
    config_data = None

    with open(config_file_path) as handle:
        config_data = json.loads(handle.read())

    colors.print_blue("installing all the taps")
    # install all brew taps
    for tap in config_data["taps"]:
        subprocess.call(["brew", "tap", tap])
    colors.print_green("installed all taps successfully")

    colors.print_blue("installing all the formulae")
    # install all brew formulae
    for formula in config_data["formulae"]:
        subprocess.call(["brew", "install", formula])
    colors.print_green("installed all formulae successfully")

    colors.print_blue("installing all the casks")
    # install all brew casks
    for cask in config_data["casks"]:
        subprocess.call(["brew", "cask", "install", cask])
    colors.print_green("installed all casks successfully")

    colors.print_blue("installing all the pip modules")
    # install all pip3 packages
    for module in config_data["pip"]:
        subprocess.call(["pip3", "install", module])
    colors.print_green("installed all pip modules successfully")

    colors.print_blue("installing all the npm packages")
    # install all npm packages
    # npm packages are installed in `~/.node_modules`
    # this prevents using `sudo` cmd for every install
    subprocess.call("mkdir", "{}/.node_modules".format(str(pathlib.Path.home())))
    colors.print_yellow("created {}/.node_modules".format(str(pathlib.Path.home())))

    # change npm prefix
    subprocess.call("npm", "config", "set", "prefix",
                    "{}/.node_modules".format(str(pathlib.Path.home())))

    for package in config_data["npm"]:
        subprocess.call(["npm", "install", "--global", package])
    colors.print_green("installed all npm packages successfully")

    colors.print_blue("creating all the directories")
    # create home directory structure
    for entry in config_data["home_directory"]:
        subprocess.call(
            ["mkdir", "-p", "{}/{}".format(str(pathlib.Path.home()), entry)])
    colors.print_green("successfully created all the directories")
