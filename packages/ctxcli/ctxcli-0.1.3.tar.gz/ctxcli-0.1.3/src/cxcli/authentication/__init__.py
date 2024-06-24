import argparse
from cxcli.cx_caller import ENVS, CxCaller, get_domain_name
from cxcli.authentication.auth import write_token_env_to_config
from cxcli.cx_token import get_token
from rich.console import Console
from rich import print

def auth_cmd():
    console = Console()
    env = ""
    tenant = ""
    u = ""
    p = ""
    while env not in ENVS:
        env = console.input(f"Please enter [bold yellow]enviroment[/] ({','.join(ENVS)}):")
    while tenant == "":
        tenant = console.input("Please enter [bold yellow]tenant[/]:")
    while u == "":
        u = console.input("Please enter [bold yellow]username[/]:")
    while p == "":
        p = console.input("Please enter [bold yellow]password[/]:",password=True)
    domain_name = get_domain_name(env)
    print("Authenticating...")
    try:
        access_token, refresh_token, expires_in = get_token(u, p, tenant, domain_name)
        write_token_env_to_config(access_token=access_token,env=env, tenant=tenant, refresh_token=refresh_token, expires_in=expires_in)
        print("[bold green]Success[/]. You can now run the CLI again with any command")
    except Exception as ex:
        print(f"[bold red]{str(ex)}[/]")
    
