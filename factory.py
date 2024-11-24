class User:
    """
    Base class representing a generic library user.
    """
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        """
        Returns a dictionary of permissions for the user.
        Overridden by subclasses.
        """
        return {"max_books": 0, "can_manage_library": False}


class Student(User):
    """
    Represents a student user with specific permissions.
    """
    def get_permissions(self):
        return {"max_books": 3, "can_manage_library": False}


class Teacher(User):
    """
    Represents a teacher user with specific permissions.
    """
    def get_permissions(self):
        return {"max_books": 10, "can_manage_library": False}


class Librarian(User):
    """
    Represents a librarian user with specific permissions.
    """
    def get_permissions(self):
        return {"max_books": float("inf"), "can_manage_library": True}


class UserFactory:
    """
    Factory class to create different types of users based on input.
    """
    @staticmethod
    def create_user(user_type, name):
        if user_type == "Student":
            return Student(name)
        elif user_type == "Teacher":
            return Teacher(name)
        elif user_type == "Librarian":
            return Librarian(name)
        else:
            raise ValueError(f"Unknown user type: {user_type}")