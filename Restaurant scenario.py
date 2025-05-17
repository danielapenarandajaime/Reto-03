class Menultem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_price(self, *args: "Menultem") -> float:
        sum: float = self.price

        for i in args:
            sum += i.price
        return f"The total price is {sum}"
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Beverages(Menultem):
    def __init__(self, name, price, alcohol: bool):
        super().__init__(name, price)
        self.alcohol = alcohol
        

class Starters(Menultem):
    def __init__(self, name, price, portion: str):
        super().__init__(name, price)
        self.portion = portion


class MainCourse(Menultem):
    def __init__(self, 
                name, 
                price, 
                protein: str, 
                spicy: bool, 
                vegetarian: bool):
        super().__init__(name, price)
        self.protein = protein
        self.spicy = spicy
        self.vegetarian = vegetarian


class Desserts(Menultem):
    def __init__(self, 
                name, 
                price, 
                level_sugar: str, 
                gluten_free: bool):
        super().__init__(name, price)
        self.level_sugar = level_sugar
        self.gluten_free = gluten_free


class Extras(Menultem):
    def __init__(self, name, price, with_sausage: bool):
        super().__init__(name, price)
        self.with_sausage = with_sausage
        

class KidsMenu(Menultem):
     def __init__(self, name, price, haealthy: bool):
        super().__init__(name, price)
        self.healthy = haealthy

class Order:
    def __init__(self, *args: Menultem):
        self.items = [*args]
    
    def add_items(self, item: "Menultem"):
        self.items.append(item)
    
    def bill_amount(self) -> float:
        sum = 0
        for i in self.items:
            sum += i.price
        return sum
    
    def discount(self, percent: float) -> float:
        total: float = self.bill_amount()
        discounted: float = total * percent / 100
        return discounted
    
    def print_bill(self, percent: float):
        for item in self.items:
            print(f"{item}")

        subtotal = self.bill_amount()
        discount = self.discount(percent)
        total = subtotal - discount

        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Total Due: ${total:.2f}")


menu = Order(
            Beverages("Coke", 5.4, False), 
             Beverages("Wine", 20, True), 
             Beverages("Appel Juice", 6.2, False), 
             Starters("Spring rolls", 10.45, "Small"), 
             Starters("Soup", 5.8, "Medium"), 
             MainCourse("Spaghetti Bolognese", 16.7, "Meat", False, False),
             MainCourse("Curry", 18, "Tofu", True, True),
             MainCourse("Grilled salmon with vegetables", 20, "Salmon", False, False),
             Desserts("Cheesecake", 8.9,"Medium", False),
             Desserts("Strawberry Donut", 4.67, "High", True),
             Extras("French Fries", 6.98, True),
             KidsMenu("Pizza", 11.76, False))
menu.add_items(Extras("Salad", 4.5, False))
menu.print_bill(10)
main_course1 = MainCourse("Spaghetti Bolognese", 16.7, "Meat", False, False)
main_course2 = MainCourse("Curry", 18, "Tofu", True, True)
main_course3 = MainCourse("Grilled salmon with vegetables", 20, "Salmon", False, False)
dessert1 = Desserts("Strawberry Donut", 4.67, "High", True)
dessert2 = Desserts("Cheesecake", 8.9,"Medium", False)
beverage1 = Beverages("Coke", 5.4, False)
beverage2 = Beverages("Wine", 20, True)
beverage3 = Beverages("Appel Juice", 6.2, False)

print(main_course1.total_price(main_course2, main_course3))
print(dessert1.total_price(dessert2))
print(beverage1.total_price(beverage2, beverage3))

        