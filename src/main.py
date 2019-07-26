# Created by Nikhil Anand <nick.muj.programmer@gmail.com>
#
# This module initializes the installation process on the
# detected platform. It provides the necessary information to
# the user before starting a new stage. 

import os
import platform
from packages import colors
from packages.os_platform.osx.osx_installer import osx_installer

if platform.system() == "Darwin":
    colors.print_blue("MacOS {}".format(platform.mac_ver()[0]))
    osx_installer(
        os.path.join(os.path.dirname(__file__), "../config/osx_config.json"))
else:
    colors.print_yellow("System Not Supported")