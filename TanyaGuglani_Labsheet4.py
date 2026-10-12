import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")

# Create and select database
cursor.execute("CREATE DATABASE IF NOT EXISTS LibraryDB")
cursor.execute("USE LibraryDB")

# Drop existing tables to refresh the data
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("DROP TABLE IF EXISTS Borrowing")
cursor.execute("DROP TABLE IF EXISTS Books")
cursor.execute("DROP TABLE IF EXISTS Students")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# Create Students table
cursor.execute("""
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    department VARCHAR(100)
)
""")

# Create Books table
cursor.execute("""
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    book_title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    price DECIMAL(10,2)
)
""")

# Create Borrowing table
cursor.execute("""
CREATE TABLE Borrowing (
    borrow_id INT PRIMARY KEY,
    student_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)
""")

# Insert Students
cursor.execute("""
INSERT INTO Students VALUES
(1, 'Tanya', 'tanya.guglani@gmail.com', 'Computer Science'),
(2, 'Ananya Verma', 'ananya.verma@gmail.com', 'Information Technology'),
(3, 'Rohan Gupta', 'rohan.gupta@gmail.com', 'Electronics')
""")

# Insert Books
cursor.execute("""
INSERT INTO Books VALUES
(201, 'Python for Beginners', 'John Smith', 450.00),
(202, 'Data Structures and Algorithms', 'Robert Lafore', 650.00),
(203, 'SQL Fundamentals', 'Alan Beaulieu', 500.00)
""")

# Insert Borrowing records
cursor.execute("""
INSERT INTO Borrowing VALUES
(101, 1, 201, '2026-10-01', NULL),
(102, 2, 202, '2026-10-03', NULL),
(103, 3, 203, '2026-10-05', '2026-10-10')
""")

# Save changes
connection.commit()

# Display Students
cursor.execute("SELECT * FROM Students")
print("\nStudents:")
for row in cursor.fetchall():
    print(row)

# Display Books
cursor.execute("SELECT * FROM Books")
print("\nBooks:")
for row in cursor.fetchall():
    print(row)

# Display Borrowing records
cursor.execute("SELECT * FROM Borrowing")
print("\nBorrowing:")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()

print("\nConnection closed.")
