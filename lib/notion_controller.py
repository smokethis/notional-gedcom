"""Module for interacting with the Notion API."""

import os
import json
import requests

NOTION_KEY = os.environ.get("NOTION_KEY")
headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def search_databases():
    """Search for databases using a Notion integration."""
    # Define search parameters
    search_params = {"filter": {"value": "database", "property": "object"}}
    # Make the request
    try:
        search_response = requests.post(
            "https://api.notion.com/v1/search",
            json=search_params,
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)
    # print(search_response.json())
    # Get the database ID
    database_id = search_response.json()["results"][0]["id"]
    # Return variables
    return database_id


def get_db(db_id):
    """Get info for a given Notion database."""
    try:
        db_response = requests.get(
            f"https://api.notion.com/v1/databases/{db_id}",
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)
    print(db_response.json())


def query_db(db_id):
    """Query a Notion database for all records."""
    try:
        query_response = requests.post(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)
    print(query_response.json())


def create_db_row(db_id):
    """Create a new row in a Notion database."""
    # Define the data
    data = {
        "parent": {"database_id": db_id},
        "properties": {
            "FirstName": {"title": [{"text": {"content": "Reginald"}}]},
            "LastName": {"rich_text": [{"text": {"content": "BUMBAGS"}}]},
        },
    }
    # Make the request
    try:
        requests.post(
            "https://api.notion.com/v1/pages",
            json=data,
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)


db_id = search_databases()
# get_db(db_id)
# print("============")
# query_db(db_id)
create_db_row(db_id)
