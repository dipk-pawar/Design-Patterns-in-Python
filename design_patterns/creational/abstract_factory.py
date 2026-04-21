"""
Abstract Factory Design Pattern

Intent: Lets you produce families of related objects without specifying their 
concrete classes.

👍 Pros:
- Guaranteed compatibility: You can be sure that the products you get from a factory are compatible with each other.
- Loose coupling: Avoids tight coupling between concrete products and client code.
- Single Responsibility Principle: Product creation code is centralized, making the code easier to support.
- Open/Closed Principle: You can introduce new variants of products without breaking existing client code.

👎 Cons:
- Complexity: The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

🧩 When to Use:
- When your code needs to work with various families of related products, but you don't want it to depend on the concrete classes of those products (they might be unknown beforehand or you simply want to allow future extensibility).
- When you have a class with a set of Factory Methods that blur its primary responsibility.
"""
from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT PRODUCTS
# ==========================================
# These are the interfaces for a family of distinct but related products.

class Button(ABC):
    """
    Abstract Product A
    """
    @abstractmethod
    def paint(self) -> str:
        """Render the button"""
        pass


class Checkbox(ABC):
    """
    Abstract Product B
    """
    @abstractmethod
    def paint(self) -> str:
        """Render the checkbox"""
        pass


# ==========================================
# 2. CONCRETE PRODUCTS
# ==========================================
# These are the specific implementations of abstract products, grouped by variants.

class MacButton(Button):
    def paint(self) -> str:
        return "Rendering a macOS style Button."

class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a macOS style Checkbox."


class WindowsButton(Button):
    def paint(self) -> str:
        return "Rendering a Windows style Button."

class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "Rendering a Windows style Checkbox."


# ==========================================
# 3. ABSTRACT FACTORY
# ==========================================
class GUIFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family.
    """
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================
# Concrete Factories produce a family of products that belong to a single variant.
# The factory guarantees that resulting products are compatible. Note that
# signatures of the Concrete Factory's methods return an abstract product, while
# inside the method a concrete product is instantiated.

class MacFactory(GUIFactory):
    """
    Produces macOS style GUI elements.
    """
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class WindowsFactory(GUIFactory):
    """
    Produces Windows style GUI elements.
    """
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


# ==========================================
# 5. CLIENT CODE
# ==========================================
class Application:
    """
    The client code works with factories and products only through abstract types:
    GUIFactory, Button, and Checkbox. This allows passing any factory or product
    subclass to the client code without breaking anything.
    """
    def __init__(self, factory: GUIFactory) -> None:
        self.factory = factory
        # Create products belonging strictly to the provided factory's family
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def render_ui(self) -> str:
        """Use the abstract products' methods without knowing their concrete classes."""
        results = [
            self.button.paint(),
            self.checkbox.paint()
        ]
        return "\n".join(results)


if __name__ == "__main__":
    print("--- Abstract Factory Pattern Example ---\n")
    
    # Normally, the application chooses the factory type depending on 
    # configuration or environment settings.
    os_type = "mac" # Try changing this to "windows"
    
    factory: GUIFactory
    if os_type == "mac":
        factory = MacFactory()
    else:
        factory = WindowsFactory()
        
    app = Application(factory)
    print(f"App initialized with os_type='{os_type}':")
    print(app.render_ui())
    
    print("\n--- Changing environment to Windows ---")
    app_windows = Application(WindowsFactory())
    print(app_windows.render_ui())
