import csv
from cxcli import USER_SERVICE_NAME, BUSINESS_UNIT_SERVICE_NAME
from cxcli.cx_caller import CxCaller, Verb
from rich import print
import time
from tqdm import tqdm
import pandas as pd

# Define mandatory fields

MANDATORY_FIELDS = ['business_unit_id', 'username']


def get_users(cx: CxCaller):
    users_raw = cx.call(verb=Verb.GET, service=USER_SERVICE_NAME, path="users?returnAll=true")
    users = users_raw["response"]["Users"]
    return users


def get_business_unit(cx: CxCaller, id):
    business_units = cx.call(verb=Verb.GET, service=BUSINESS_UNIT_SERVICE_NAME, path="businessUnit")
    id_exists = any(bu.get("id") == id for bu in business_units)
    return id_exists

    
def add_user_to_business_unit(cx: CxCaller, bu_id, user_id):
    payload = {"Users": [{"Id": f"{user_id}"}]}
    add_user_response = cx.call(verb=Verb.POST, service=USER_SERVICE_NAME, path=f"businessUnits/{bu_id}/members", payload=payload)
    return add_user_response


def check_mandatory_fields(row, idx):
    missing_fields = [field for field in MANDATORY_FIELDS if not row.get(field)]
    if missing_fields:
        print(f'Error in row {idx}: Missing mandatory fields {missing_fields}')
        return False
    return True

def process_row(cx: CxCaller, row, idx, all_users):    
    # Check mandatory field
    if not check_mandatory_fields(row, idx):
        return 1
                        
    # Check if user exists
    username = row.get('username')
    user_id = next((user["Id"] for user in all_users if user["Username"] == username), None)
    if user_id is None:
        # print(f"user '{username}' does not exist.")
        return 1
    
    
    # Check if Business Unit Id exists
    bu_id = row.get('business_unit_id')
    id_exists = get_business_unit(cx, bu_id)
    if id_exists == False:
        # print(f"{bu_id} not found.")
        return 1
        
    # Add user to business unit
    if user_id and bu_id:
        add_user_response = add_user_to_business_unit(cx, bu_id, user_id)
        if add_user_response.get("message") == "Success":
            return 0
        else:
            return 1
    else:
        print(f'Error: Invalid user ID or business unit ID for row {row}')
        return 1


def add_users(cx: CxCaller, file):
    csv_file_path = file
    
    print(f"Starting to process data from {csv_file_path}...")
    row_count = len(pd.read_csv(csv_file_path)) 
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as input:
        csvreader = csv.DictReader(input)
        
        all_users = get_users(cx)
        
        successful_count = 0
        unsuccessful_count = 0
        rows = enumerate(csvreader, start=2)
        
        for idx, row in tqdm(rows,total=row_count,desc="Processing rows",colour="green"):
            result = process_row(cx, row, idx, all_users)
            if result == 0:
                successful_count += 1
            else:
                unsuccessful_count += 1

        print(f"[bold green]{successful_count} users have been added successfully.[/]")
        if unsuccessful_count > 0:
            print(f"[bold red]{unsuccessful_count} user{'s' if unsuccessful_count > 1 else ''} could not be added. Please recheck the data and retry.[/]")   
