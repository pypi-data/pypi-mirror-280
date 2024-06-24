import argparse
from cxcli.cx_caller import CxCaller
from cxcli.migration.migration_files_cmd import migration_files_cmd
from cxcli.migration.migration_records_cmd import migration_records_cmd
from cxcli.tenant.list_tenants import list_tenants


def usage():
    print ("Available commands: list")


def create_parser():
    parser = argparse.ArgumentParser(description="Users")
    parser.add_argument("cmd", choices=["file","record"])
    parser.add_argument("params", nargs="*")
    return parser



def migration_cmd(cx: CxCaller, format, args):
    parsed_args = create_parser().parse_args(args=args)
    cmd = parsed_args.cmd
    if cmd=="file":
        migration_files_cmd(cx,format,parsed_args.params)
    if cmd =="record":
        migration_records_cmd(cx,format,parsed_args.params)
