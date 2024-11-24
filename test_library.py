from singleton import LibraryCatalog
from observer import UserObserver
from factory import UserFactory
from facade import LibraryInterface

def test_library_system():
    print("=== Singleton Test ===")
    catalog = LibraryCatalog()  
    catalog.add_book("Book A")
    catalog.add_book("Book B")

    print("Current books in catalog:", catalog.get_books())
    print()

    print("=== Adapter Test ===")
    json_data = '{"title": "Book C", "author": "Author C", "year": 2023}'
    csv_data = "title,author,year\nBook D,Author D,2022"
    xml_data = """
    <book>
        <title>Book E</title>
        <author>Author E</author>
        <year>2021</year>
    </book>
    """
    catalog.import_book_from_json(json_data)
    catalog.import_book_from_csv(csv_data)
    catalog.import_book_from_xml(xml_data)
    print("Books after importing from various formats:", catalog.get_books())
    print()

    print("=== Factory Test ===")
    student = UserFactory.create_user("Student", "Alice")
    teacher = UserFactory.create_user("Teacher", "Bob")
    librarian = UserFactory.create_user("Librarian", "Clara")
    print(f"{student.name} ({student.__class__.__name__}): {student.get_permissions()}")
    print(f"{teacher.name} ({teacher.__class__.__name__}): {teacher.get_permissions()}")
    print(f"{librarian.name} ({librarian.__class__.__name__}): {librarian.get_permissions()}")
    print()

    print("=== Observer Test ===")
    observer1 = UserObserver("Alice")
    observer2 = UserObserver("Bob")
    catalog.add_observer(observer1)
    catalog.add_observer(observer2)
    catalog.add_book("Book F")
    catalog.remove_book("Book A")
    catalog.return_book("Book A")
    print()

    print("=== Facade Test ===")
    library_interface = LibraryInterface()
    library_interface.register_user("Student", "John")
    library_interface.add_book("Book G")
    library_interface.add_book("Book H")
    library_interface.add_book("Book I")
    library_interface.add_book("Book J")

    library_interface.borrow_book("John", "Book G") 
    library_interface.borrow_book("John", "Book H")
    library_interface.borrow_book("John", "Book I")

    library_interface.borrow_book("John", "Book J")

    library_interface.return_book("John", "Book H")
    library_interface.borrow_book("John", "Book J")

    library_interface.list_books()
    library_interface.list_users()
    print()

    print("=== Iterator Test ===")
    print("Iterating through books:")
    book_iterator = catalog.get_book_iterator()
    for book in book_iterator:
        print(f"- {book}")
    print("\nIterating through users:")
    user_iterator = library_interface.get_user_iterator()
    for user in user_iterator:
        print(f"- {user.name} ({user.__class__.__name__})")
    print()


if __name__ == "__main__":
    test_library_system()
