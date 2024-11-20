from iterator import BookIterator  
from observer import UserObserver  
from adapter import BookAdapter    

class LibraryCatalog:
    """
    Singleton class to represent the library catalog.
    Ensures there is only one instance of the catalog in the system.
    """
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = []  
            cls._instance.observers = []  
        return cls._instance

    # Observer
    def add_observer(self, observer):
        """
        Adds an observer to the library catalog.
        :param observer: Observer, the observer to add
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Removes an observer from the library catalog.
        :param observer: Observer, the observer to remove
        """
        self.observers.remove(observer)

    def notify(self, message):
        """
        Notifies all observers with a message.
        :param message: str, the notification message
        """
        for observer in self.observers:
            observer.update(message)

    def add_book(self, book):
        """
        Adds a book to the catalog and notifies observers.
        :param book: str, name of the book to add
        """
        self.books.append(book)
        self.notify(f"Book '{book}' has been added to the catalog.")

    def remove_book(self, book):
        """
        Removes a book from the catalog and notifies observers.
        :param book: str, name of the book to remove
        """
        if book in self.books:
            self.books.remove(book)
            self.notify(f"Book '{book}' has been borrowed.")
        else:
            print(f"Book '{book}' is not available in the catalog.")

    def return_book(self, book):
        """
        Returns a book to the catalog and notifies observers.
        :param book: str, name of the book to return
        """
        self.books.append(book)
        self.notify(f"Book '{book}' has been returned to the catalog.")

    # Adapter
    def import_book_from_json(self, json_data):
        """
        Imports a book from JSON format using the adapter.
        :param json_data: str, JSON string containing book data
        """
        book = BookAdapter.from_json(json_data)
        self.add_book(book["title"])

    def import_book_from_csv(self, csv_data):
        """
        Imports a book from CSV format using the adapter.
        :param csv_data: str, CSV string containing book data
        """
        book = BookAdapter.from_csv(csv_data)
        self.add_book(book["title"])

    def import_book_from_xml(self, xml_data):
        """
        Imports a book from XML format using the adapter.
        :param xml_data: str, XML string containing book data
        """
        book = BookAdapter.from_xml(xml_data)
        self.add_book(book["title"])

    # Iterator
    def get_book_iterator(self):
        """
        Returns an iterator for the list of books.
        """
        return BookIterator(self.books)

    def get_books(self):
        """
        Returns the list of books in the catalog.
        :return: list of books
        """
        return self.books