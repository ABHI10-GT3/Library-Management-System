from .add_remove_books import add_book, remove_book, update_book
from .search_borrow_books import search_books, borrow_book
from .manage_users import add_user, view_users
from .return_books import return_book
from .issue_management import check_overdue_books, notify_user

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Update a book")
        print("4. Search for books")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Add a new user")
        print("8. View all users")
        print("9. Check overdue books")
        print("10. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, isbn, quantity)
        elif choice == "2":
            isbn = input("Enter ISBN to remove: ")
            remove_book(isbn)
        elif choice == "3":
            isbn = input("Enter ISBN to update: ")
            title = input("Enter new title (leave empty to skip): ")
            author = input("Enter new author (leave empty to skip): ")
            quantity = input("Enter new quantity (leave empty to skip): ")
            update_book(isbn, title, author, quantity if quantity else None)
        elif choice == "4":
            query = input("Enter book title, author, or ISBN to search: ")
            books = search_books(query)
            for book in books:
                print(book)
        elif choice == "5":
            user_id = int(input("Enter your user ID: "))
            isbn = input("Enter ISBN of the book to borrow: ")
            print(borrow_book(user_id, isbn))
        elif choice == "6":
            user_id = int(input("Enter your user ID: "))
            isbn = input("Enter ISBN of the book to return: ")
            print(return_book(user_id, isbn))
        elif choice == "7":
            username = input("Enter username: ")
            email = input("Enter email: ")
            add_user(username, email)
        elif choice == "8":
            users = view_users()
            for user in users:
                print(user)
        elif choice == "9":
            overdue_books = check_overdue_books()
            for overdue in overdue_books:
                notify_user(overdue["title"], overdue["username"])
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")