import argparse
from cxcli.cx_caller import CxCaller
from cxcli.tenant.list_tenants import list_tenants


def usage():
    print ("Available commands: list")


def create_parser():
    parser = argparse.ArgumentParser(description="Users")
    parser.add_argument("cmd", choices=["list"])
    parser.add_argument("params", nargs="*")
    return parser



def tenants_cmd(cx: CxCaller, format, args):
    parsed_args = create_parser().parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd=="list":
        list_tenants(cx,format,parsed_args)
