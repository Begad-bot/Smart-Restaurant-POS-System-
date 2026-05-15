# 🍔 Smart Restaurant POS System


 video explanation:https://youtu.be/fUqtfYBoAUU
A professional, terminal-based cashier system built with Python, demonstrating advanced Object-Oriented Programming (OOP) concepts.

## 🚀 Features

- **Interactive Terminal Menu:** Easy-to-use interface for viewing the menu, adding items, and printing receipts.
- **Dynamic Menu Items:** Supports multiple categories including **Food** and **Beverages**, each with unique properties.
- **Smart Pricing Engine:** Automatically calculates taxes, service fees, and discounts based on the item type.
- **Data Protection:** Robust validation ensures that prices and availability statuses cannot be set to illogical values.
- **Professional Receipt Output:** Generates a clean, formatted digital ticket for the customer.

## 🛠️ Technical Implementation (OOP)

This system was built adhering to strict structural requirements:

1.  **Abstraction (The Blueprint):** Uses the `abc` module to define a `MenuItem` base class. This ensures all menu items implement `calculate_final_price()` and `display_info()`.
2.  **Specialization (Inheritance):**
    *   **FoodItem:** Adds `allergy_info`. Implements a logic where a **15% service fee** is added to the base price.
    *   **BeverageItem:** Adds `size`. Implements a **50% "Happy Hour" discount** but adds a **$0.50 sugar tax**.
3.  **Encapsulation (Data Protection):** Sensitive attributes like `price` are protected using Python `@property` decorators. Attempting to set a negative price will trigger a validation error.
4.  **Polymorphism (Smart Behavior):** The `CustomerOrder` handles a list of generic `MenuItem` objects. When printing the receipt, it calls the same method on every item, yet each item calculates its price according to its own unique business rules.

## 💻 How to Run

### Prerequisites
- Python 3.6 or higher installed on your system.

### Execution
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

```powershell
python Smart Restaurant (POS) System.py
```

## 📝 Example Usage

1. **View Menu:** See all available food and drinks with their base prices and specific details (allergies/size).
2. **Add to Order:** Input the ID (e.g., `1`) or the Name (e.g., `Burger`) to add it to your current session.
3. **Print Receipt:** View the final breakdown. 
   * *Example:* A $12.00 Burger becomes **$13.80** after the service fee.
   * *Example:* A $3.00 Cola becomes **$2.00** after the Happy Hour discount and sugar tax.

---
*Developed as part of a Python OOP demonstration.*
