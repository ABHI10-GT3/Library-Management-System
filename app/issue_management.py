from .db import get_db_connection, commit_and_close
from datetime import datetime

# Check overdue books and generate notifications
def check_overdue_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.title, u.username, br.borrow_date 
        FROM borrow br 
        JOIN books b ON br.book_id = b.id 
        JOIN users u ON br.user_id = u.id 
        WHERE br.return_date IS NULL AND strftime('%s', CURRENT_DATE) - strftime('%s', br.borrow_date) > 604800
    """)  # 604800 seconds = 7 days (1 week)

    overdue_books = cursor.fetchall()
    conn.close()
    return overdue_books

# Issue notification (simple print for now)
def notify_user(book_title, username):
    print(f"Notification: '{book_title}' borrowed by {username} is overdue!")