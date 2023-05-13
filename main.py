"""Main function"""

from lib.time_machine import TimeMachinePerson
import lib.notion_controller as notion_controller
from lib.ged4py import GedcomReader, date as ged4pydate


def gedcom_date_to_tuple(ged_date: object) -> tuple:
    """Converts a GEDCOM date to a tuple of date components.

    Parameters
    ----------
        ged_date (DateValueSimple): A GEDCOM formatted date to convert.

    Returns
    -------
        tuple_date (tuple): A tuple of date components in the format (YYYY, MM, DD).
    """
    if ged_date is not None:
        # Split the date into its components
        # date_components = ged_date.split()
        # Convert the month to a number
        if isinstance(ged_date, ged4pydate.DateValueSimple):
            month = {
                "JAN": 1,
                "FEB": 2,
                "MAR": 3,
                "APR": 4,
                "MAY": 5,
                "JUN": 6,
                "JUL": 7,
                "AUG": 8,
                "SEP": 9,
                "OCT": 10,
                "NOV": 11,
                "DEC": 12,
            }[ged_date.date.month]
            # Create the Notion date
            tuple_date = (ged_date.date.year, month, ged_date.date.day)
        if isinstance(ged_date, ged4pydate.DateValuePhrase):
            # Split the date into its components
            date_components = ged_date.phrase.split(" ")
            month = {
                "January": 1,
                "February": 2,
                "March": 3,
                "April": 4,
                "May": 5,
                "June": 6,
                "July": 7,
                "August": 8,
                "September": 9,
                "October": 10,
                "November": 11,
                "December": 12,
            }[date_components[1]]
            # Create the Notion date
            tuple_date = (date_components[0], month, date_components[2])
        # Return the Notion date
        return tuple_date
    else:
        # Return None if there is no date
        return None


def create_time_machine_person(individual) -> object:
    """Receive a GEDCOM individual record and create a TimeMachinePerson object

    Parameters
    ----------
        individual (ged4py.model.Record): A GEDCOM individual record.

    Returns
    -------
        thisperson (TimeMachinePerson): A TimeMachinePerson object.
    """

    # Create a TimeMachinePerson object
    thisperson = TimeMachinePerson(gedcom_ref=individual.xref_id)
    # Set the person's name
    thisperson.FullBirthName = individual.name.format()
    # Set the person's birth and death dates
    thisperson.BirthDeath = (
        gedcom_date_to_tuple(individual.sub_tag_value("BIRT/DATE")),
        gedcom_date_to_tuple(individual.sub_tag_value("DEAT/DATE")),
    )
    # Set the person's birth and death places
    thisperson.PlaceOfBirth = individual.sub_tag_value("BIRT/PLAC")
    thisperson.PlaceOfDeathBurial = individual.sub_tag_value("DEAT/PLAC")
    # Set the person's gender
    thisperson.Gender = indi.sex
    # Return the TimeMachinePerson object
    return thisperson


# db_id = notion_controller.search_databases()
# notion_controller.get_db(db_id)
# print("============")
# notion_controller.query_db(db_id)
# notion_controller.post_dbpage_update(db_id)

PATH = "Sample.ged"
with GedcomReader(PATH) as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        print(indi)
        globals()[indi.xref_id] = create_time_machine_person(indi)

print("============")
