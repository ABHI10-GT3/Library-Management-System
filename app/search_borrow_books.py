from .db import get_db_connection, commit_and_close

# Search books by title, author, or ISBN
def search_books(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%"))
    
    books = cursor.fetchall()
    conn.close()
    return books

# Borrow a book (assuming user_id is known)
def borrow_book(user_id, isbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
    book = cursor.fetchone()
    
    if book and book["quantity"] > 0:
        cursor.execute("INSERT INTO borrow (user_id, book_id) VALUES (?, ?)", (user_id, book["id"]))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book["id"],))
        commit_and_close(conn)
        return f"Book '{book['title']}' borrowed successfully!"
    else:
        conn.close()
        return "Book not available."