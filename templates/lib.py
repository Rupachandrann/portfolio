class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_title):
        if book_title in self.books:
            self.books[book_title] += 1
            print(f"{book_title} has been added. Total copies: {self.books[book_title]}")
        else:
            self.books[book_title] = 1
            print(f"{book_title} has been added. Total copies: 1")

    def get_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("Available books in the library:")
            for book_title, count in self.books.items():
                print(f"{book_title} - Total copies: {count}")

    def return_book(self, book_title):
        if book_title in self.books:
            self.books[book_title] += 1
            print(f"{book_title} has been returned. Total copies: {self.books[book_title]}.")
        else:
            print(f"{book_title} is not in the library.")

    def view_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("All books in the library:")
            for book_title, count in self.books.items():
                print(f"{book_title} - Total copies: {count}")

    def remove_book(self, book_title):
        if book_title in self.books:
            if self.books[book_title] > 1:
                self.books[book_title] -= 1
                print(f"{book_title} has been removed. Total copies: {self.books[book_title]}.")
            else:
                del self.books[book_title]
                print(f"{book_title} has been removed from the library.")
        else:
            print(f"{book_title} is not in the library.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Get List of Available Books")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Remove Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_title = input("Enter the title of the book to add: ")
            library.add_book(book_title)
        elif choice == '2':
            library.get_books()
        elif choice == '3':
            book_title = input("Enter the title of the book to return: ")
            library.return_book(book_title)
        elif choice == '4':
            library.view_books()
        elif choice == '5':
            book_title = input("Enter the title of the book to remove: ")
            library.remove_book(book_title)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
