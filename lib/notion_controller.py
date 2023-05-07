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


def search_databases() -> str:
    """Search for databases using a Notion integration.
    Returns:
        database_id (str): The ID of the database."""
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


def get_db(db_id: str):
    """Get info for a given Notion database.
    Parameters:
        db_id (str): The ID of the database to get."""
    try:
        db_response = requests.get(
            f"https://api.notion.com/v1/databases/{db_id}",
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)
    print(db_response.json())


def query_db(db_id: str):
    """Query a Notion database for all records.
    Parameters:
        db_id (str): The ID of the database to query."""
    try:
        query_response = requests.post(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            headers=headers,
            timeout=15,
        )
    except requests.exceptions.HTTPError as err:
        print(err)
    print(query_response.json())


def post_dbpage_update(db_id: str):
    """Update a row in a Notion database.
    Parameters:
        db_id (str): The ID of the database to update."""
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
