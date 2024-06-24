import argparse
import json

from rich import print_json
from cxcli import SRV_MIGRATION, SRV_TENANT, USER_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich.console import Console
from rich.table import Table


def as_table(file_id, records):
    table = Table(title=f'Records for file "{file_id}"')
    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column(
        "Data",
        style="cyan",
        no_wrap=False,
    )
    table.add_column("Status", justify="center", style="magenta")
    table.add_column("Last Update", justify="center", style="blue")
    table.add_column("Error", justify="center", style="red", no_wrap=False)
    table.add_column("Party Id", justify="center", style="yellow")
    for r in records:
        table.add_row(
            r["recordId"],
            r["data"],
            r["status"],
            r["lastUpdate"],
            r["err"],
            r["partyId"],
        )

    console = Console()
    console.print(table)


def create_parser():
    parser = argparse.ArgumentParser(description="migration files ")
    parser.add_argument("cmd", choices=["list"])
    parser.add_argument("file_id")
    # parser.add_argument(
    #     "status",
    #     help="Filter by status",
    #     choices=["pending", "in progress", "fail", "done"],
    #     default="done",
    # )
    return parser


def list_records(cx: CxCaller, format: str, file_id):
    # records = cx.call(verb=Verb.GET, service=SRV_MIGRATION, path=f"records/{file_id}/status/{status}")
    records = cx.call(verb=Verb.GET, service=SRV_MIGRATION, path=f"records/{file_id}")
    if format == "table":
        as_table(file_id=file_id, records=records)
    else:
        print_json(data=records)


def migration_records_cmd(cx: CxCaller, format, args):
    parsed_args = create_parser().parse_args(args=args)
    if parsed_args.cmd == "list":
        list_records(cx=cx, format=format, file_id=parsed_args.file_id)
    return
    a = cx.call(verb=Verb.GET, service=SRV_MIGRATION, path="files")
    print(a)
    return
    tenants = a["children"]
