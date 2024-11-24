class BookIterator:
    """
    Iterator for iterating through the list of books in the library catalog.
    """
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            result = self.books[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class UserIterator:
    """
    Iterator for iterating through the list of users in the library system.
    """
    def __init__(self, users):
        self.users = list(users.values())  
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.users):
            result = self.users[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        