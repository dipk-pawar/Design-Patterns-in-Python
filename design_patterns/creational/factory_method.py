"""
Factory Method Design Pattern

Intent: Define an interface for creating an object, but let subclasses 
alter the type of objects that will be created.

👍 Pros:
- Single Responsibility Principle: Product creation code is centralized.
- Open/Closed Principle: You can introduce new types of products without breaking existing frontend/client code.
- Loose Coupling: Avoids tight coupling between the creator class and concrete products.

👎 Cons:
- Increased Complexity: The code may become more complicated since you need to introduce many new subclasses to implement the pattern.

🧩 When to Use:
- When you don't know beforehand the exact types and dependencies of the objects your code should work with.
- When you want to provide users of your library or framework with a way to extend its internal components seamlessly.
- When you want to save system resources by reusing existing objects instead of rebuilding them (e.g. Connection pooling).
"""
from abc import ABC, abstractmethod


# ==========================================
# 1. PRODUCT INTERFACE & CONCRETE PRODUCTS
# ==========================================
class Transport(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    """
    Concrete Product A: Implements the Transport interface.
    """
    def deliver(self) -> str:
        return "Delivering cargo by land in a box."


class Ship(Transport):
    """
    Concrete Product B: Implements the Transport interface.
    """
    def deliver(self) -> str:
        return "Delivering cargo by sea in a container."


# ==========================================
# 2. CREATOR INTERFACE & CONCRETE CREATORS
# ==========================================
class Logistics(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """
    
    @abstractmethod
    def create_transport(self) -> Transport:
        """
        The factory method pattern relies on this method being overridden by subclasses
        to instantiate appropriate Transport objects.
        """
        pass

    def plan_delivery(self) -> str:
        """
        Note: The Creator's primary responsibility is NOT just creating products. 
        Usually, it contains core business logic that relies on the Product objects
        returned by the factory method.
        """
        # Call the factory method to create a Product object.
        transport = self.create_transport()
        
        # Now, use the product's standardized interface.
        result = f"Logistics: The creator's plan delivery just worked with -> '{transport.deliver()}'"
        return result


class RoadLogistics(Logistics):
    """
    Concrete Creator A: Overrides the factory method to return a Truck.
    """
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    """
    Concrete Creator B: Overrides the factory method to return a Ship.
    """
    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    # Example Usage demonstrating how client code operates cleanly.
    
    print("--- Factory Method Pattern Example ---\n")
    
    # Client doesn't need to manually instantiate Trucks or Ships, 
    # it delegates that to the specific Logstics creators.
    road_logistics = RoadLogistics()
    sea_logistics = SeaLogistics()
    
    print("App: Planning logistics for Land Transport...")
    print(road_logistics.plan_delivery())
    
    print("\nApp: Planning logistics for Sea Transport...")
    print(sea_logistics.plan_delivery())
