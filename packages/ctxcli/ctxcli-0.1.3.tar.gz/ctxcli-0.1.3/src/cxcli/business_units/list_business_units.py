import json
from rich import print_json
from cxcli import BUSINESS_UNIT_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich.console import Console
from rich.table import Table

def as_table(business_units):
    table = Table(title="Business Units")

    table.add_column("Id", style="cyan", no_wrap=True)
    table.add_column("Name", style="cyan", no_wrap=True,)
    table.add_column("ExternalId", style="cyan", no_wrap=True)
    table.add_column("Description", style="cyan", no_wrap=True)
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Parent", style="cyan", no_wrap=True)
    for b in business_units:
        parent_id = b["childOf"].get("id", None) if "childOf" in b else None
        parent_name = next((bu["name"] for bu in business_units if bu["id"] == parent_id), None)
        table.add_row(
            b.get("id", None),
            b.get("name", None),
            b.get("externalId", None),
            b.get("description", None),
            b["businessUnitSpec"].get("buType", None),
            parent_name
        )

    console = Console()
    console.print(table)
    

def list_business_units(cx: CxCaller, format):
    business_units = cx.call(verb=Verb.GET, service=BUSINESS_UNIT_SERVICE_NAME, path="businessUnit")
    if format =="table":
        as_table(business_units=business_units)
    else:
        print_json(data=business_units)
