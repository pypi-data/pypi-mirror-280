import json
from cxcli import SRV_TENANT, USER_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich.console import Console
from rich.table import Table
from rich import print_json



def as_table(tenants):
    table = Table(title="Tenants")
    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Name", style="cyan", no_wrap=True,)
    table.add_column("Brand", style="cyan", no_wrap=True,)
    table.add_column("Created", justify="center", style="magenta")
    for t in tenants:
        brand_name = None
        if "public" in t and "branding" in t["public"]:
            brand_name = t["public"]["branding"]["brandName"]
        table.add_row(
            t["id"],
            t["name"],
            brand_name,
            t["createDate"]
        )

    console = Console()
    console.print(table)


def list_tenants(cx: CxCaller, format, params):
    a = cx.call(verb=Verb.GET, service=SRV_TENANT, path="tenant")
    tenants = a["children"]
    if format =="table":
        as_table(tenants=tenants)
    else:
        print_json(data=tenants)