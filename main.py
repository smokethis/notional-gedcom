"""Main function"""

import lib.notion_controller as notion_controller

db_id = notion_controller.search_databases()
# get_db(db_id)
# print("============")
# query_db(db_id)
notion_controller.post_dbpage_update(db_id)
