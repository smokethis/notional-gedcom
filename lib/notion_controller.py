"""Module for interacting with the Notion API."""

import os
import time
import requests
from typing import TypedDict


NOTION_KEY = os.environ.get("NOTION_KEY")
headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


class NotionTimeMachinePerson(TypedDict):
    """Class for a Notion Time Machine person.
    Properties:
        Brief_Biography (str): A brief biography of the person.
        Notable_Figure (bool): Whether the person is a notable figure.
        Notes (str): Notes about the person.
        Dates_Approx (bool): Whether the dates are approximate.
        Branch (str): The branch of the family tree.
        Spouse (str): The spouse of the person.
        Images (str): Images of the person.
        Parents (str): The parents of the person.
        Siblings (str): The siblings of the person.
        Library (str): The library of the person.
        Children (str): The children of the person.
        Siblings (str): The siblings of the person.
        Place_of_Death_Burial (str): The place of death or burial of the person.
        Tags (str): Tags for the person.
        Associated_With (str): People associated with the person.
        Display_Name (str): The display name of the person.
        Nickname (str): The nickname of the person.
        Place_of_Birth (str): The place of birth of the person.
        Gender (str): The gender of the person. (M/F)
        Birth_Death (str): The birth and death dates of the person.
        Marriage (str): The marriage date of the person.
        Title (str): The title of the person.
        Alt_Names (str): The alternate names of the person.
        Full_Name (str): The full name of the person.
    """

    Brief_Biography: str
    Notable_Figure: bool
    Notes: str
    Dates_Approx: bool
    Branch: str
    Spouse: str
    Images: str
    Parents: str
    Siblings: str
    Library: str
    Children: str
    Siblings: str
    Place_of_Death_Burial: str
    Tags: str
    Associated_With: str
    Display_Name: str
    Nickname: str
    Place_of_Birth: str
    Gender: str
    Birth_Death: str
    Marriage: str
    Title: str
    Alt_Names: str
    Full_Name: str


def search_databases() -> str:
    """Search for databases using a Notion integration.
    Returns:
        database_id (str): The ID of the database."""
    # Define search parameters
    search_params = {"filter": {"value": "database", "property": "object"}}
    # Make the request
    while True:
        try:
            search_response = requests.post(
                "https://api.notion.com/v1/search",
                json=search_params,
                headers=headers,
                timeout=15,
            )
        except requests.exceptions.HTTPError as err:
            print(err)
        if search_response.status_code == 429:
            print(
                "The Notion API is rate-limited. Trying again in {} seconds....".format(
                    search_response.headers["Retry-After"]
                )
            )
            time.sleep(int(search_response.headers["Retry-After"]))
        else:
            break

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
