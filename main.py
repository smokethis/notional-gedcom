"""Main function"""

import lib.notion_controller as notion_controller
from lib.notion_controller import NotionTimeMachinePerson
from lib.ged4py import GedcomReader


# db_id = notion_controller.search_databases()
# notion_controller.get_db(db_id)
# print("============")
# notion_controller.query_db(db_id)
# notion_controller.post_dbpage_update(db_id)

PATH = "Sample.ged"
with GedcomReader(PATH) as parser:
    # GedcomReader provides context support
    for i, indi in enumerate(parser.records0("INDI")):
        print(indi)
        thisperson = NotionTimeMachinePerson()
        thisperson.set_property_value("Full Name", indi.name.format())
        thisperson.set_property_value("Birth Date", indi.sub_tag_value("BIRT/DATE"))
        thisperson.set_property_value("Place of Birth", indi.sub_tag_value("BIRT/PLAC"))
        thisperson.set_property_value("Death Date", indi.sub_tag_value("DEAT/DATE"))
        thisperson.set_property_value(
            "Place of Death / Burial", indi.sub_tag_value("DEAT/PLAC")
        )
        thisperson.set_property_value("Gender", indi.sex)
