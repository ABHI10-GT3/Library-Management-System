import sqlite3

# Database connection
def get_db_connection():
    conn = sqlite3.connect('library_management.db')
    conn.row_factory = sqlite3.Row  # Allows column names to be accessed as keys
    return conn

# Commit changes and close the connection
def commit_and_close(conn):
    conn.commit()
    conn.close()