import abc

class MenuItem(abc.ABC):
    """
    Requirement 1: The Blueprint
    An abstract base class representing any item on the menu.
    """
    def __init__(self, name, price):
        self._name = name
        self._price = 0
        self.price = price  # Use setter for validation
        self._is_available = True

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        """Requirement 3: Data Protection and Validation"""
        if not isinstance(value, (int, float)) or value < 0:
            print(f"Error: Invalid price '{value}' for {self._name}. Price must be a positive number.")
            return
        self._price = value

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        """Requirement 3: Data Protection and Validation"""
        if not isinstance(value, bool):
            print(f"Error: Availability must be True or False.")
            return
        self._is_available = value

    @abc.abstractmethod
    def calculate_final_price(self):
        """To be implemented by subclasses"""
        pass

    @abc.abstractmethod
    def display_info(self):
        """To be implemented by subclasses"""
        pass


class FoodItem(MenuItem):
    """
    Requirement 2: Specialization (Type A)
    Adds 'allergy_info' property.
    """
    def __init__(self, name, price, allergy_info="None"):
        super().__init__(name, price)
        self.allergy_info = allergy_info

    def calculate_final_price(self):
        """Requirement 4: Food applies a 15% service fee."""
        service_fee = self.price * 0.15
        return self.price + service_fee

    def display_info(self):
        return f"[Food] {self.name:<20} | Base: ${self.price:>6.2f} | Allergies: {self.allergy_info}"


class BeverageItem(MenuItem):
    """
    Requirement 2: Specialization (Type B)
    Adds 'size' property.
    """
    def __init__(self, name, price, size="Medium"):
        super().__init__(name, price)
        self.size = size

    def calculate_final_price(self):
        """Requirement 4: Beverages apply 50% Happy Hour discount + $0.50 sugar tax."""
        discount = self.price * 0.50
        sugar_tax = 0.50
        return (self.price - discount) + sugar_tax

    def display_info(self):
        return f"[Bev]  {self.name:<20} | Base: ${self.price:>6.2f} | Size: {self.size}"


class CustomerOrder:
    """Requirement 4: Dedicated CustomerOrder structure"""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_order(self):
        if not self.items:
            print("\nYour order is empty.")
            return
        print("\n--- Current Order ---")
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item.name} - ${item.price:.2f}")

    def print_receipt(self):
        """Requirement 4: Polymorphic calculation of final price"""
        if not self.items:
            print("\nCannot print receipt for an empty order.")
            return

        print("\n" + "="*40)
        print("          RESTAURANT RECEIPT          ")
        print("="*40)
        
        total = 0
        for item in self.items:
            final_price = item.calculate_final_price()
            total += final_price
            print(f"{item.name:<25} ${final_price:>8.2f}")
            # Optional: Show breakdown if needed, but keeping it clean like a ticket
            
        print("-" * 40)
        print(f"{'TOTAL (inc. Taxes/Fees):':<25} ${total:>8.2f}")
        print("="*40)
        print("     Thank you for dining with us!    ")
        print("="*40 + "\n")


class CashierSystem:
    """Requirement 5: Terminal Interaction and Main Loop"""
    def __init__(self):
        self.menu = [
            FoodItem("Burger", 12.00, "Gluten, Dairy"),
            FoodItem("Salad", 8.50, "None"),
            FoodItem("Pasta", 14.00, "Gluten"),
            BeverageItem("Cola", 3.00, "Large"),
            BeverageItem("Coffee", 4.50, "Medium"),
            BeverageItem("Orange Juice", 5.00, "Small")
        ]
        self.current_order = CustomerOrder()

    def display_menu(self):
        print("\n" + "-"*10 + " RESTAURANT MENU " + "-"*10)
        for idx, item in enumerate(self.menu, 1):
            print(f"[{idx}] {item.display_info()}")
        print("-" * 37)

    def run(self):
        print("Welcome to the Python Restaurant Cashier System!")
        
        while True:
            print("\n[1] View Menu")
            print("[2] Add Item to Order")
            print("[3] View Current Order")
            print("[4] Print Final Receipt")
            print("[5] Exit")
            
            choice = input("\nPlease select an option: ").strip()
            
            try:
                if choice == "1":
                    self.display_menu()
                elif choice == "2":
                    self.display_menu()
                    item_input = input("Enter the Item ID or Name to add: ").strip()
                    
                    found_item = None
                    # Try to match by index
                    if item_input.isdigit():
                        idx = int(item_input) - 1
                        if 0 <= idx < len(self.menu):
                            found_item = self.menu[idx]
                    
                    # Try to match by name if not found by index
                    if not found_item:
                        for item in self.menu:
                            if item.name.lower() == item_input.lower():
                                found_item = item
                                break
                    
                    if found_item:
                        self.current_order.add_item(found_item)
                        print(f"Added {found_item.name} to your order.")
                    else:
                        print("Error: Item not found. Please check the ID or Name.")
                        
                elif choice == "3":
                    self.current_order.view_order()
                elif choice == "4":
                    self.current_order.print_receipt()
                elif choice == "5":
                    print("Exiting system. Have a great day!")
                    break
                else:
                    print("Invalid selection. Please choose a number between 1 and 5.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")

if __name__ == "__main__":
    system = CashierSystem()
    system.run()
