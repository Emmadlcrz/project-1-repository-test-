# ============================================================
# TASK 1: ENCAPSULATION (10 Points)
# ============================================================
class MenuItem:
    def __init__(self, item_id: str, name: str, base_price: float, rating: float = 5.0):
        self.__item_id = item_id
        self.__rating = rating
        self.name = name
        self.base_price = base_price

    def get_item_id(self):
        return self.__item_id

    def get_rating(self):
        return self.__rating

    def set_rating(self, new_rating: float):
        if 1.0 <= new_rating <= 5.0:
            self.__rating = new_rating
        else:
            print("Invalid rating! Must be between 1.0 and 5.0.")

    def calculate_price(self):
        return self.base_price

    def get_details(self):
        return f"{self.name} - P{self.calculate_price():.2f} (Rating: {self.__rating:.1f}/5.0)"


# ============================================================
# TASK 2: INHERITANCE, OVERRIDING & OVERLOADING (20 Points)
# ============================================================
class PizzaItem(MenuItem):
    def __init__(self, item_id: str, name: str, base_price: float, size: str):
        super().__init__(item_id, name, base_price)
        self.size = size
        self.toppings = []

    # Method Overloading via Default Parameter
    def add_topping(self, topping_name: str, extra_cost: float = 10.00):
        self.toppings.append(topping_name)
        self.base_price += extra_cost

    # Method Overriding
    def calculate_price(self):
        if self.size == "Small":
            return self.base_price
        elif self.size == "Medium":
            return self.base_price + 25.00
        elif self.size == "Large":
            return self.base_price + 50.00
        return self.base_price

    # Method Overriding
    def get_details(self):
        topping_count = len(self.toppings)
        return (
            f"({self.size}) {self.name} (with {topping_count} topping(s)) - "
            f"P{self.calculate_price():.2f} (Rating: {self.get_rating():.1f}/5.0)"
        )


class DrinkItem(MenuItem):
    def __init__(self, item_id: str, name: str, base_price: float, is_cold: bool):
        super().__init__(item_id, name, base_price)
        self.is_cold = is_cold

    # Method Overriding
    def calculate_price(self):
        if self.is_cold:
            return self.base_price + 1.00
        return self.base_price

    # Method Overriding
    def get_details(self):
        temp_label = "(Cold)" if self.is_cold else "(Hot)"
        return (
            f"{temp_label} {self.name} - Php{self.calculate_price():.2f} "
            f"(Rating: {self.get_rating():.1f}/5.0)"
        )


# ============================================================
# TASK 3: POLYMORPHISM (10 Points)
# ============================================================
class FoodOrder:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.calculate_price()
        return total

    def print_receipt(self):
        print(f"\n>>MegaBites Receipt for {self.customer_name}")
        print("-" * 50)
        for item in self.items:
            print(item.get_details())
        print("-" * 50)
        print(f"Total Amount Due: P{self.calculate_total():.2f}")


# ============================================================
# TEST & VERIFICATION (10 Points)
# ============================================================
if __name__ == "__main__":
    print(">>1. Testing Encapsulation")
    pizza = PizzaItem("P01", "Pepperoni Pizza", 200.00, "Large")
    pizza.set_rating(4.0)    # Valid update
    pizza.set_rating(6.5)    # Invalid: Should display error message!

    print("\n>>2. Testing Method Overloading")
    pizza.add_topping("Extra Cheese")
    pizza.add_topping("Smoked Bacon", 20.00)

    print("\n>>3. Testing Inheritance & Polymorphism")
    drink = DrinkItem("D01", "C2 Green Tea", 15.00, True)

    order = FoodOrder("Leslie")
    order.add_item(pizza)
    order.add_item(drink)

    order.print_receipt()