"""
Singleton Design Pattern

Intent: Ensure a class only has one instance and provide a global point of
access to it.

👍 Pros
- Controlled access: Certainty that a class only has a single, globally accessible instance.
- Lazy Initialisation: The instance is initialized only upon the first request (unlike global variables).
- Thread safety: The metaclass implementation ensures robust behavior over concurrent environments.

👎 Cons
- Violates Single Responsibility Principle: The pattern tries to solve two problems simultaneously (managing object creation logic and fulfilling business logic).
- Difficult to test: Because it introduces heavy global state to an application, unit testing Singleton components (mocking them) can get complicated.
- Hidden Dependencies: Components that utilize the Singleton implicitly bind themselves to a deeply nested component rather than extracting an explicit dependency path.

🧩 When to Use
- When caching data or establishing heavy initialisation routines where recreation of objects is vastly expensive (e.g., establishing Database Connections to an active pool).
- If your program requires stricter control over global variables or shared resources (e.g., System loggers, global application configuration routers).
"""
import threading
from typing import Any


class SingletonMeta(type):
    """
    A thread-safe implementation of Singleton using a metaclass.
    This pattern ensures that any class using this metaclass will result
    in only one active object instance.
    """
    _instances: dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # Double-checked locking pattern for optimal performance and thread safety
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """
    Example class representing a Database Connection using the Singleton pattern.
    """
    def __init__(self) -> None:
        # In a real app, database initialization logic goes here.
        self.connection_string = "Connected to the database."
        
    def query(self, sql: str) -> str:
        return f"Executing Query: {sql}"


if __name__ == "__main__":
    # Example Usage
    print("--- Singleton Pattern Example ---")
    
    # Both variables will point to the same object
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 memory address: {id(db1)}")
    print(f"db2 memory address: {id(db2)}")
    print(f"Are db1 and db2 the exact same instance? {'Yes' if db1 is db2 else 'No'}")
    
    # Using the connection
    print(db1.query("SELECT * FROM users;"))
