# Install python-dotenv package
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()


# Usage in your application
from log_data import *
from custom_development_standardisation import generate_outcome_message
import os
import requests

# Define the URL of the API endpoint
db_log_instance = custom_logger()
db_log_instance.initialise_database()
# Make the GET request


# Check if the request was successful

api_key = os.getenv('api_key')
print(f'Your API key is {api_key}')
x = "8a862259e3a14dc58e00ebb034267bea"
baseURL = "https://api.notion.com/v1/databases/"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}
data = {
    "filter": {},
    "sorts": []
}

def get_database(id):
    db_log_instance.store_log()
    response = requests.post(f'https://api.notion.com/v1/databases/{id}/query',headers=headers)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return generate_outcome_message('success',data)
    else:
        return generate_outcome_message("error",response.text,the_type="others")

def extract_data_from_properties(property_object):
    db_log_instance.store_log()
    extract = {}
    for column_name,obj in property_object.items():
        if obj["type"] == "rich_text":
            if len(obj['rich_text']) >= 1:
                extract[column_name] = obj["rich_text"][0]['plain_text']
        if obj["type"] == "title":
            if len(obj["title"]) >= 1:
                extract[column_name] = obj["title"][0]['plain_text']
        if obj["type"] == "number":
            extract[column_name] = obj["number"]
    return generate_outcome_message('success',extract)


def extract_core_row_data_from_table(results):
    db_log_instance.store_log()
    table_data = []
    for row in results:
        outcome = extract_data_from_properties(row["properties"])["output"]
        outcome["url"] = row["url"]
        table_data.append(outcome)
    return generate_outcome_message('success',table_data)

def extract_specific_row(core_rows,column_name,value):
    db_log_instance.store_log()
    for i in core_rows:
        # print(i)
        if i[column_name] == value:
            return i
    return False



# outcome = get_database(x,baseURL)
# # print(outcome)
# final = extract_row_data_from_table(results=outcome["results"])
# for i in final:
#     print("------")
#     for key,value in i.items():
#         print(key, ":", value)
# https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]

