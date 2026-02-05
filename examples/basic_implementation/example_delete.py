import skypydb
from skypydb.errors import TableAlreadyExistsError

# Create a client
client = skypydb.Client()

# Create tables from the schema
# This reads the schema from skypydb/schema.py and creates all tables
try:
    tables = client.create_table()
# if the tables already exists the programe get them instead
except TableAlreadyExistsError:
    tables = {
        "success": client.get_table("success"),
        "warning": client.get_table("warning"),
        "error": client.get_table("error"),
    }

# Access your tables
success_table = tables["success"]
warning_table = tables["warning"]
error_table = tables["error"]

# delete data on the table assuming they are already data in the table.
success_table.delete(
    component="AuthService",
    user_id="user123"
)
