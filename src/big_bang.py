import os
import sys
import emoji

modules_path = os.getcwd() + "/src/modules"
configs_path = os.getcwd() + "/config"

sys.path.extend(
    [modules_path, modules_path + "/cli", modules_path + "/platform_code"])

import cli_parser  # pylint: disable=import-error
import cli_colors  # pylint: disable=import-error

import osx_installer  # pylint: disable=import-error

args = cli_parser.parse_args()

config_json = configs_path + '/osx_config.json'
if args.config is not None:
    config_json = args.config

if args.platform == "osx":
    cli_colors.success("starting OSX installation")
    osx_installer.osx_init(config_json)
elif args.platform == 'linux':
    if args.distro == None:
        print('need linux distro information, see --help')
        sys.exit(0)
    else:
        print(emoji.emojize(":construction_worker: work in progress"))
        print(
            "visit https://github.com/muj-programmer/big-bang for more infomation"
        )
else:
    print(emoji.emojize(":construction_worker: work in progress"))
    print(
        "visit https://github.com/muj-programmer/big-bang for more infomation")
