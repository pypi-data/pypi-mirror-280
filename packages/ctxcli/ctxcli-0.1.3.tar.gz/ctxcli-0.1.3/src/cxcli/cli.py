import argparse
import warnings

from cxcli import users
from cxcli import authentication
from cxcli import business_units
from cxcli.authentication.auth import get_token_from_config, get_auth_config_field
from cxcli.cx_caller import ENVS, CxCaller, get_domain_name
from cxcli.migration import migration_cmd
from cxcli.tenant import tenants_cmd
from urllib3.exceptions import InsecureRequestWarning
from rich import print
from rich.console import Console

def create_parser():
    parser = argparse.ArgumentParser(
        description="ConnectX CLI", epilog="Copyright Amdocs"
    )
    parser.add_argument("--t", "--tenant", help="Tenant name")
    parser.add_argument("--u", "--user", help="ConnectX username (email in most cases)")
    parser.add_argument("--p", "--passw", help="ConnectX password")
    parser.add_argument(
        "--e",
        "--env",
        help=",".join(ENVS),
        choices=ENVS,
        type=str.lower,
    )
    parser.add_argument(
        "--format", default="table", choices=["json", "csv", "table"], type=str.lower
    )
    parser.add_argument("command", choices=["user","tenant","migration", "auth", "business-unit"], type=str.lower)
    parser.add_argument('--file', type=str, help='File path for input file to be processed')
    parser.add_argument("params", nargs="*")
    return parser


def main():
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    args = create_parser().parse_args()
    if args.command == "auth":
        authentication.auth_cmd()
        return
    results = get_token_from_config()
    access_token = results[1]
    env = results[2]
    
    if not access_token:
        return
    domain_name = get_domain_name(env)
    cx = CxCaller(domain_name=domain_name, token=access_token)
    format = args.format
    if args.command == "user":
        users.users_cmd(cx, format, args.params)
    elif args.command == "tenant":
        tenants_cmd(cx, format, args.params)
    elif args.command =="migration":
        migration_cmd(cx,format,args.params)
    elif args.command == "business-unit":
        business_units.bu_cmd(cx, format, args.params, args.file)
    else:
        raise ValueError(f"Unknown command {args.command}")
    # print(token)
