# Function to add a new book
def add_book():
    with open("library.txt", "a") as file:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        file.write(book_id + "," + title + "," + author + "\n")
        print("Book added successfully!")


# Function to display all books
def display_books():
    try:
        with open("library.txt", "r") as file:
            print("\nLibrary Catalogue:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No books found!")


# Function to search books
def search_book():
    search = input("Enter book title or author: ").lower()

    with open("library.txt", "r") as file:
        found = False
        for line in file:
            if search in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("Book not found!")


# Function to generate reports
def generate_report():
    try:
        with open("library.txt", "r") as file:
            books = file.readlines()

        print("\nTotal number of books:", len(books))

        author = input("Enter author name: ").lower()
        count = 0

        for book in books:
            details = book.strip().split(",")
            if len(details) == 3 and details[2].lower() == author:
                count += 1

        print("Books by", author, ":", count)

    except FileNotFoundError:
        print("No books found!")


# Main program
while True:
    print("\n--- Library Catalogue ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")