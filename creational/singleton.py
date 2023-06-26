"""
    Creational Design Pattern
    -------------------------
    Creational design patterns are a category of software design patterns that focus on object creation mechanisms.
    These patterns provide solutions to various object creation problems and help ensure that objects are created in a
    flexible, reusable, and efficient manner. Creational design patterns address the process of object instantiation,
    hiding the complexity of object creation, and promoting loose coupling between objects.

    Singleton
    ---------
    This pattern ensures that a class has only one instance and provides a global point of access to it.
    It is useful when you need to restrict the instantiation of a class to a single object,
    such as a logging or database connection class.

    - All descriptions and comments created by ChatGPT and GitHub Copilot
"""


class Database:
    """
        Database class
    """

    __instance = None  # Private instance

    @staticmethod
    def getinstance():
        """
            Static access method
            :return: Database
        """
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self) -> None:
        """
            Virtually private constructor

            :raise Exception: This class is a singleton!
        """
        if Database.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self

    def connect(self) -> None:
        """
            Connect to database
        :return: None
        """
        pass

    # Other methods ...


if __name__ == "__main__":
    db1 = Database.getinstance()
    db2 = Database.getinstance()

    print(db1 is db2)  # True
