import argparse
import emoji


def parse_args():
    parser = argparse.ArgumentParser(
        prog="bigbang",
        usage="%(prog)s [options] <platform>",
        description="automate the configuration of your new workstation",
        epilog=
        "visit https://github.com/muj-programmer/big-bang for more infomation")

    parser.add_argument("platform",
                        help="specify the current host platform",
                        choices=["osx", "linux", "windows"])

    parser.add_argument(
        "--distro",
        help="linux distribution [used when platform=\"linux\"]",
        choices=["arch", "debian"])

    parser.add_argument("--config",
                        help="path to external config file",
                        type=argparse.FileType('r'))

    return parser.parse_args()