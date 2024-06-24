import json

from rich import print_json
from cxcli import USER_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich.console import Console
from rich.table import Table


def as_table(users):
    table = Table(title="Users")

    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Username", style="cyan", no_wrap=True,)
    table.add_column("Status", style="cyan", no_wrap=True)
    table.add_column("Enabled", style="cyan", no_wrap=True)
    table.add_column("Created", justify="center", style="magenta")
    table.add_column("Last modified", justify="center", style="magenta")
    for u in users:
        table.add_row(
            u["Id"],
            u["Username"],
            u["UserStatus"],
            str(u["Enabled"]),
            u["UserCreatedDate"],
            u["UserLastModifiedDate"],
        )

    console = Console()
    console.print(table)


def list_users(cx: CxCaller, format, params):
    a = cx.call(verb=Verb.GET, service=USER_SERVICE_NAME, path="users?returnAll=true")
    # a = call_cx(token=token,verb=Verb.GET,service="user-management")
    users = a["response"]["Users"]
    if format =="table":
        as_table(users=users)
    else:
        print_json(data=users)
