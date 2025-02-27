library = {}  # Dictionary to store books (book_name: availability)

def add_book():
    book = input("Enter book name: ")
    library[book] = "Available"
    print(f'"{book}" added to library.')

def view_books():
    if not library:
        print("No books in the library.")
    else:
        print("\nLibrary Books:")
        for book, status in library.items():
            print(f"{book} - {status}")

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library and library[book] == "Available":
        library[book] = "Issued"
        print(f'You have issued "{book}".')
    else:
        print("Book not available or already issued.")

def return_book():
    book = input("Enter book name to return: ")
    if book in library and library[book] == "Issued":
        library[book] = "Available"
        print(f'"{book}" returned successfully.')
    else:
        print("Invalid return request.")

def main():
    while True:
        print("\nLibrary Management")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()