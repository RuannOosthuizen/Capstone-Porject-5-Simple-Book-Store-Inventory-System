#====Libraries====#

import sqlite3


#====Creating the database and table====#

# Here the database and cursor is defined.
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

#Here the table is created and defined.
cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)")


#====Initial books to be inserted into database====#

initial_books = [(3001, 'A Tale of Two Cities', 'Charlse Dickens', 30),
                 (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
                 (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
                 (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
                 (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

# Inserting the "initial_books" into the table.
cursor.executemany('INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?)', initial_books)


#====Functions====#

# Function to display the database to the user.
def display_database():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Function to add a book to the database.
def add_book():
    print("To add a book please fill in the details below:\n")

    # Asking the user for the books information.
    title = input("Please enter the title of the book:\n ")
    author = input("Please enter the name of the Aurthor:\n ")
    quantity = int(input("Please enter the quentity of this book stored:\n "))

    # Here the new book is added to the database.
    cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES (?, ?, ?)", (title, author, quantity))
    conn.commit()

    print(f"The book {title}, by {author} has been added to the database.")


# Function to update a books detials.
def update_book():
    print("Please select a book you wish to cahnge by the typing in the id:\n")

    # Displaying the database to the user for book selection.
    display_database()

    # The user can now select a book by its id number.
    book_id = int(input("Please type in the Books id NO:\n "))

    print("To update a books information please fill in the detials below:\n")

    # Asking the user for the new details of the book.
    new_title = input("Please fill in the new Title of this book:\n ")
    new_author = input("Please fill in the new Author of this book:\n ")
    new_quantity = int(input("Please fill in the quantity of this book:\n "))

    # Updating the selected books details.
    cursor.execute("UPDATE book SET Title = ?, Author = ?, Qty = ? WHERE id = ?", (new_title, new_author, new_title, book_id))
    conn.commit()
    print(f"Bood ID {book_id} has been updated successfully.")


# Function to delete a selected book.
def delete_book():
    print("Please select a book by its ID number to delete:\n")
    id_verify = False

    # Displaying the table to the user.
    display_database()

    # The user can now select which book to delete with its id no.
    # The user is prompted to confirm the id number to make sure they want to delete the book row.
    while not id_verify:
        book_id = int(input("Please tpye in the id NO:\n "))
        confirm_id = int(input("Please confirm the id NO of the book:\n "))

        # Here the both inputs are checked to match.
        if book_id == confirm_id:
            id_verify = True
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id))
            conn.commit
            print(f"Book {book_id} has successfully been delete from the database.")

        else:
            print("ID Numbers do not match please try again.")


# Function to search for a book.
def search_books():
    print("Searching for a book:")

    # The user can enter the title or author of the desired book they want to search for.
    keyword = input("Please input the Title or the Author's name to search for:\n ")

    # Then the command is executed that searches for the book in the talbe books using the LIKE operator.
    cursor.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
    rows = cursor.fetchall()

    # Here a response is printed to the user.
    if len(rows) == 0:
        print("No matching book is found.")

    else:
        for row in rows:
            print(row)

#====Creating the Menu system for the user====#

print("Welcome to the E-Book Store Database.\n")

# Menu system for user.
while True:
    menu = int(input('''Please select one of the followng number options:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit'''))

    if menu == 1:
        add_book()

    elif menu == 2:
        update_book()

    elif menu == 3:
        delete_book()

    elif menu == 4:
        search_books()

    elif menu == 0:
        print("Goodbye")
        break

    else:
        print("Oops wrong input. Please try again.")

# The connection to the data base is closed.
conn.close()