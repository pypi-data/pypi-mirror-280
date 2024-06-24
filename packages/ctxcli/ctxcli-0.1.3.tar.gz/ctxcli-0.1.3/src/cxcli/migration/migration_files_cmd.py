import argparse
import json

from rich import print_json
from cxcli import SRV_MIGRATION, SRV_TENANT, USER_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich.console import Console
from rich.table import Table


def as_table(files):
    table = Table(title="Files")
    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Name", style="cyan", no_wrap=True,)
    table.add_column("Created", justify="center", style="magenta")
    table.add_column("records", justify="center", style="blue")
    table.add_column("pending", justify="center", style="blue")
    table.add_column("in progress", justify="center", style="yellow")
    table.add_column("done", justify="center", style="green")
    table.add_column("fail", justify="center", style="red")
    table.add_column("status", justify="center")
    for f in files:
        table.add_row(
            f["fileId"],
            f["fileName"],
            f["received"],
            str(f["records"]),
            str(f["byStatus"]["pending"]),
            str(f["byStatus"]["in progress"]),
            str(f["byStatus"]["done"]),
            str(f["byStatus"]["fail"]),
            f["status"]
        )

    console = Console()
    console.print(table)

def create_parser():
    parser = argparse.ArgumentParser(description="migration files ")
    parser.add_argument("cmd", choices=["list"])
    return parser

def list_files(cx: CxCaller, format:str):
    files = cx.call(verb=Verb.GET, service=SRV_MIGRATION, path="files")
    if format =="table":
        as_table(files=files)
    else:
        print_json(data=files)
    

def migration_files_cmd(cx: CxCaller, format, args):
    parsed_args = create_parser().parse_args(args=args)
    if parsed_args.cmd == "list":
        list_files(cx=cx,format=format)
    return
    a = cx.call(verb=Verb.GET, service=SRV_MIGRATION, path="files")
    print(a)
    return
    tenants = a["children"]
