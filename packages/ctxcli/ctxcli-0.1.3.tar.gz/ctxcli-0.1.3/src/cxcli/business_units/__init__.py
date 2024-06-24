import argparse
import sys
import os
from cxcli.business_units.add_users import add_users
from cxcli.business_units.list_business_units import list_business_units
from cxcli.cx_caller import CxCaller

def usage():
    print("Available commands: add_users")

def create_parser():
    parser = argparse.ArgumentParser(description="Business Units")
    parser.add_argument("cmd", choices=["add-users", "list"])
    return parser

def bu_cmd(cx: CxCaller, format, args, file=None):
    parser = create_parser()
    parsed_args = parser.parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd == "list":
        list_business_units(cx, format)
    if cmd == "add-users":
        if not file:
            print("Error: No file specified. Please provide a file path after the --file option.")
            sys.exit(1)
        absolute_path = os.path.abspath(file)
        if not os.path.exists(absolute_path):
            print(f"Error: The file {absolute_path} does not exist.")
            sys.exit(1)
        filename, file_extension = os.path.splitext(absolute_path)
        if file_extension.lower() != '.csv':
            print(f"Error: The file {absolute_path} is not a CSV file.")
            sys.exit(1)
        add_users(cx, absolute_path)