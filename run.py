from app.cli import main
from app.db import get_db_connection

# Initialize the database and tables
conn = get_db_connection()
# Create tables if they don't exist (optional step)
# Create tables()  # Uncomment if necessary to create tables

# Start the command-line interface
if __name__ == "__main__":
    main()
