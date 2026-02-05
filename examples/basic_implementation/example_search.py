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

# Ensure there is at least one row to demonstrate search
success_table.add(
    component="AuthService",
    action="login",
    message="User logged in successfully",
    user_id="user123"
)

# Search results by filter
user_success_logs = success_table.search(
    user_id="user123"
)

if not user_success_logs:
    print("No results found.")
else:
    for user_success_log in user_success_logs:
        print(user_success_log)
