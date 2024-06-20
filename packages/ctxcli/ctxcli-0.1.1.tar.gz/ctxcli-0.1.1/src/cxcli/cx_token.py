import requests
import json
import os
from cachetools import cached, TTLCache


@cached(cache=TTLCache(maxsize=2, ttl=3600))
def get_token(username, password, tenant, dbs_domain_name): 
    proxy_url = os.getenv("PROXY")
    proxy = None
    if (proxy_url):
        proxy = {
            "http": proxy_url,
            "https": proxy_url
        }
    url = f"https://cognito.{dbs_domain_name}/auth/initiate"
    payload = {
        "Username": username,
        "Password": password, 
        "TenantName": tenant,
        "ApplicationClient": "catalog"
        }
    headers = {
        "Content-Type": "application/json"
    }

    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=proxy)
    response.raise_for_status()    
    
    ACCESS_TOKEN = (response.json()["AccessToken"])
    REFRESH_TOKEN = (response.json()["RefreshToken"])
    EXPIRES_IN = (response.json()["ExpiresIn"])
        
    return ACCESS_TOKEN, REFRESH_TOKEN, EXPIRES_IN


def get_refreshed_token(tenant, dbs_domain_name,application_client_id,refresh_token): 
    proxy_url = os.getenv("PROXY")
    proxy = None
    if (proxy_url):
        proxy = {
            "http": proxy_url,
            "https": proxy_url
        }
    
    if not application_client_id:   
        url = f"https://cognito.{dbs_domain_name}/auth/idplinks?Mode=Care&TenantName={tenant}&ApplicationClient=catalog&RedirectURI=''"
    
        response = requests.request("GET", url, verify=False, proxies=proxy)
        response.raise_for_status()
        application_client_id = (response.json()["ApplicationClientId"])
    
    
    url = "https://cognito-idp.us-east-1.amazonaws.com/"
    payload = {
        "ClientId": application_client_id,
        "AuthFlow": "REFRESH_TOKEN_AUTH", 
        "AuthParameters": {
        "REFRESH_TOKEN": refresh_token
    }
        }
    headers = {
        "Content-Type": "application/json",
        "x-amz-target": "AWSCognitoIdentityProviderService.InitiateAuth",
        "content-type": "application/x-amz-json-1.1"
    }
    
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload, verify=False, proxies=proxy)
    response.raise_for_status()
    access_token = (response.json()["AuthenticationResult"]["AccessToken"])
    expires_in = (response.json()["AuthenticationResult"]["ExpiresIn"])
    return access_token, application_client_id, expires_in