"""
Main entry point for running betterlib with -m - Parses the command line arguments and runs the appropriate function.
"""

import sys
import argparse
from . import config, logging, ip, quik

logger = logging.Logger("betterlib.log", "betterlib")

conf = config.ConfigFile("config.json")

parser = argparse.ArgumentParser(description="A library of useful functions for Python 3.5+.")
parser.add_argument("-v", "--version", action="version", version="betterlib " + conf.get("version"))
parser.add_argument("-s", "--server", action="store_true", help="Starts a Quik server in the current directory.")
parser.add_argument("-p", "--port", type=int, help="The port to listen on. Defaults to 8080.")
parser.add_argument("-i", "--ip", action="store_true", help="Prints the external IP address.")

args = parser.parse_args()

if args.server:
    server = quik.QuikServer(args.port if args.port else 8080)
    server.start()
elif args.ip:
    print("IP: " + ip.get_external_ip())
else:
    parser.print_help()