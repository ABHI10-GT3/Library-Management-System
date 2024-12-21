from .db import get_db_connection, commit_and_close

# Return a borrowed book
def return_book(user_id, isbn):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.id, b.book_id, b.return_date
        FROM borrow b
        JOIN books bk ON b.book_id = bk.id
        WHERE b.user_id = ? AND bk.isbn = ? AND b.return_date IS NULL
    """, (user_id, isbn))
    
    borrow = cursor.fetchone()
    if borrow:
        cursor.execute("UPDATE borrow SET return_date = CURRENT_DATE WHERE id = ?", (borrow["id"],))
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (borrow["book_id"],))
        commit_and_close(conn)
        return "Book returned successfully!"
    else:
        conn.close()
        return "No borrow record found."