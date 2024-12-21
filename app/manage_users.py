from .db import get_db_connection, commit_and_close

# Add a new user to the system
def add_user(username, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    commit_and_close(conn)
    print(f"User '{username}' added successfully!")

# View all users
def view_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
