from .db import get_db_connection, commit_and_close

# Add a book to the database
def add_book(title, author, isbn, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, isbn, quantity) VALUES (?, ?, ?, ?)", 
                   (title, author, isbn, quantity))
    commit_and_close(conn)
    print(f"Book '{title}' added successfully!")

# Remove a book from the database
def remove_book(isbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
    commit_and_close(conn)
    print(f"Book with ISBN '{isbn}' removed successfully!")

# Update book details
def update_book(isbn, title=None, author=None, quantity=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if title:
        cursor.execute("UPDATE books SET title = ? WHERE isbn = ?", (title, isbn))
    if author:
        cursor.execute("UPDATE books SET author = ? WHERE isbn = ?", (author, isbn))
    if quantity is not None:
        cursor.execute("UPDATE books SET quantity = ? WHERE isbn = ?", (quantity, isbn))
    commit_and_close(conn)
    print(f"Book with ISBN '{isbn}' updated successfully!")
