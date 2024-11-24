from singleton import LibraryCatalog
from observer import LibraryCatalogWithNotifications
from factory import UserFactory
from iterator import UserIterator


class LibraryInterface:
    """
    Facade class to simplify interactions with library subsystems.
    """

    def __init__(self):
        self.catalog = LibraryCatalogWithNotifications()
        self.users = {}  
        self.user_loans = {}  

    def register_user(self, user_type, name):
        """
        Register a new user in the library system.
        :param user_type: str, type of user (e.g., "Student", "Teacher", "Librarian")
        :param name: str, name of the user
        """
        user = UserFactory.create_user(user_type, name)
        self.users[name] = user
        self.user_loans[name] = []  
        print(f"User '{name}' of type '{user_type}' registered successfully.")

    def add_book(self, book):
        """
        Add a new book to the library catalog.
        :param book: str, name of the book
        """
        self.catalog.add_book(book)
        print(f"Book '{book}' added to the library.")

    def borrow_book(self, user_name, book):
        """
        Borrow a book from the library catalog.
        :param user_name: str, name of the user borrowing the book
        :param book: str, name of the book to borrow
        """
        if user_name not in self.users:
            print(f"User '{user_name}' is not registered.")
            return

        user = self.users[user_name]
        borrowed_books = self.user_loans[user_name]

        if len(borrowed_books) >= user.get_permissions()["max_books"]:
            print(f"User '{user_name}' cannot borrow more books. Limit: {user.get_permissions()['max_books']}.")
            return

        if book in self.catalog.books:
            self.catalog.remove_book(book)
            borrowed_books.append(book)
            print(f"User '{user_name}' borrowed the book '{book}'.")
        else:
            print(f"Book '{book}' is not available.")

    def return_book(self, user_name, book):
        """
        Return a book to the library catalog.
        :param user_name: str, name of the user returning the book
        :param book: str, name of the book to return
        """
        if user_name not in self.users or book not in self.user_loans[user_name]:
            print(f"User '{user_name}' did not borrow the book '{book}'.")
            return

        self.user_loans[user_name].remove(book)
        self.catalog.return_book(book)
        print(f"User '{user_name}' returned the book '{book}'.")

    def list_books(self):
        """
        List all books currently available in the library.
        """
        books = self.catalog.books
        if books:
            print("Books in the library:")
            for book in books:
                print(f"- {book}")
        else:
            print("No books are currently available.")

    def list_users(self):
        """
        List all registered users.
        """
        if self.users:
            print("Registered users:")
            for name, user in self.users.items():
                print(f"- {name} ({user.__class__.__name__})")
        else:
            print("No users are registered.")

    def get_user_iterator(self):
        """
        Returns an iterator for the list of registered users.
        """
        return UserIterator(self.users)