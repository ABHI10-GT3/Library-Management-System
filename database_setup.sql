drop database library_db;
-- Create Database
CREATE DATABASE library_db;
USE library_db;

-- Create Tables
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    available INT DEFAULT 1
);
-- Users Table (for user authentication)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Librarians Table (for librarian authentication)
CREATE TABLE librarians (
    librarian_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE borrowed_books (
    borrow_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    due_date DATE DEFAULT NULL,
    return_date DATE DEFAULT NULL,
    status ENUM('borrowed', 'returned') DEFAULT 'borrowed',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Table for overdue notifications
CREATE TABLE overdue_notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    borrow_id INT NOT NULL,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    notification_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- Changed to DATETIME with default timestamp
    status ENUM('unread', 'read') DEFAULT 'unread',
    FOREIGN KEY (borrow_id) REFERENCES borrowed_books(borrow_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
-- Insert Sample Data

-- Sample Books
INSERT INTO books (book_id, title, author, isbn, available) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', '1234567890', 3),
(2, '1984', 'George Orwell', '0987654321', 2),
(3, 'To Kill a Mockingbird', 'Harper Lee', '1122334455', 5),
(4, 'Moby Dick', 'Herman Melville', '2233445566', 4),
(5, 'The Catcher in the Rye', 'J.D. Salinger', '3344556677', 6);

-- Sample Users
INSERT INTO users (user_id, name, email, password) VALUES
(1, 'Alice', 'alice@ex.com', 'pass123'),
(2, 'Bob', 'bob@ex.com', 'pass123'),
(3, 'Charlie', 'charlie@ex.com', 'pass123');

-- Sample Librarian
INSERT INTO librarians (librarian_id, email, password) VALUES
(1, 'lib1@ex.com', 'pass111'),
(2, 'lib2@ex.com', 'pass111');
-- Sample Borrowed Books
INSERT INTO borrowed_books (user_id, book_id, borrow_date, due_date, status)
VALUES 
    (1, 1, '2024-12-10', '2024-12-24', 'borrowed'),
    (2, 2, '2024-12-05', '2024-12-19', 'borrowed'),
    (3, 3, '2024-12-01', '2024-12-15', 'returned');

-- Sample Overdue Notifications
INSERT INTO overdue_notifications (borrow_id, user_id, book_id, notification_date, status)
VALUES 
    (1, 1, 1, '2024-12-15', 'unread'),
    (2, 2, 2, '2024-12-20', 'read');

