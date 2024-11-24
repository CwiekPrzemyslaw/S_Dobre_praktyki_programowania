class Observer:
    """
    Base class for observers.
    """
    def update(self, message):
        raise NotImplementedError("Subclasses must implement the update method.")


class UserObserver(Observer):
    """
    A user who subscribes to notifications.
    """
    def __init__(self, name):
        self.name = name

    def update(self, message):
        """
        Receive notification and print it.
        :param message: str, the notification message
        """
        print(f"Notification for {self.name}: {message}")


class LibraryCatalogWithNotifications:
    """
    LibraryCatalog acting as a subject in the Observer pattern.
    """
    def __init__(self):
        self.books = []
        self.observers = []

    def add_book(self, book):
        """
        Add a book to the catalog and notify observers.
        :param book: str, the name of the book to add
        """
        self.books.append(book)
        self.notify(f"Book '{book}' has been added to the catalog.")

    def remove_book(self, book):
        """
        Remove a book from the catalog and notify observers.
        :param book: str, the name of the book to remove
        """
        if book in self.books:
            self.books.remove(book)
            self.notify(f"Book '{book}' has been borrowed.")
        else:
            print(f"Book '{book}' is not available in the catalog.")

    def return_book(self, book):
        """
        Return a book to the catalog and notify observers.
        :param book: str, the name of the book to return
        """
        self.books.append(book)
        self.notify(f"Book '{book}' has been returned and is now available.")

    def add_observer(self, observer):
        """
        Add an observer to the list of observers.
        :param observer: Observer, the observer to add
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove an observer from the list of observers.
        :param observer: Observer, the observer to remove
        """
        self.observers.remove(observer)

    def notify(self, message):
        """
        Notify all observers with a message.
        :param message: str, the notification message
        """
        for observer in self.observers:
            observer.update(message)