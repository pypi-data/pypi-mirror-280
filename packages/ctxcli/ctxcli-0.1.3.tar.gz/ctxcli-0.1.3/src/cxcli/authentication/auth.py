from pathlib import Path
import os
import configparser
from cxcli.cx_caller import get_domain_name
from cxcli.cx_token import get_refreshed_token
from rich import print
from datetime import datetime, timedelta

HOME_DIR = Path.home()
CONFIG_DIR = HOME_DIR / ".ctxcli"
CONFIG_FILE = CONFIG_DIR / "config"


def write_token_env_to_config(access_token, application_client_id=None, refresh_token=None, expires_in=None, env=None, tenant=None):
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True)

    config = configparser.ConfigParser()

    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)

    if "AUTH" not in config:
        config.add_section("AUTH")
        
    config.set("AUTH", "access_token", access_token)

    if tenant: config.set("AUTH", "tenant", tenant)
    if env: config.set("AUTH", "env", env)    
    if refresh_token: config.set("AUTH", "refresh_token", refresh_token)
    if application_client_id: config.set("AUTH", "application_client_id", application_client_id)
    if expires_in:
            expiration_time = datetime.now() + timedelta(seconds=expires_in)
            config.set('AUTH', 'expires_at', expiration_time.isoformat())
    
    
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)


def get_token_from_config():
    config = configparser.ConfigParser()
    if not CONFIG_FILE.exists():
        print("[bold red]Authentication info not found. Please login first[/]")
        return None, None, None
    config.read(CONFIG_FILE)
    tenant = config["AUTH"].get("tenant", None)
    env = config["AUTH"].get("env", None)
    access_token = config["AUTH"].get("access_token", None)
    expires_at = config['AUTH'].get('expires_at',None)

    if tenant == None or env == None or access_token == None or expires_at == None:
        print("[bold red]Config file is corrupted. Please login again[/]")
        return None, None, None
    
    if datetime.now() >= datetime.fromisoformat(expires_at):
            refresh_token = config["AUTH"].get("refresh_token", None)            
            if not refresh_token:
                print("[bold red]Config file is corrupted. Please login again[/]")
                return None, None, None
            
            application_client_id = config["AUTH"].get("application_client_id")
            try:
                access_token, application_client_id, expire_in = get_refreshed_token(tenant, get_domain_name(env),application_client_id, refresh_token)
            except Exception:
                print("[bold red]Your session has expired. Please login again[/]")
                return None, None, None
            write_token_env_to_config(access_token, application_client_id, expires_in=expire_in)
            
    return tenant, access_token, env


def get_auth_config_field(field_name):
    config = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)

        if "AUTH" in config and field_name in config["AUTH"]:
            return config["AUTH"][field_name]

    return None
