import random

#============================
#     CAFE MENU DATA
#============================

#hot drinks
HOT_DRINKS = {
    "Latte": {"small": 3.00, "medium": 3.50, "large": 4.00},
    "Cappuccino": {"small": 2.75, "medium": 3.25, "large": 3.75},
    "Mocha": {"small": 3.50, "medium": 4.00, "large": 4.50},
    "Americano": {"small": 2.25, "medium": 2.75, "large": 3.25},
    "Hot Chocolate": {"small": 2.00, "medium": 2.50, "large": 3.00},
    "Matcha Latte": {"small": 3.75, "medium": 4.25, "large": 4.75}
}

#iced drinks
ICED_DRINKS = {
    "Iced Coffee": {"small": 2.50, "medium": 3.00, "large": 3.50},
    "Iced Latte": {"small": 3.25, "medium": 3.75, "large": 4.25},
    "Iced Mocha": {"small": 3.75, "medium": 4.25, "large": 4.75},
    "Cold Brew": {"small": 3.00, "medium": 3.50, "large": 4.00},
    "Iced Matcha": {"small": 3.50, "medium": 4.00, "large": 4.50}
}

#customization (milk, syrups, and cold foam)
MILK_OPTIONS = {
    "Whole": 0.00,
    "Skim": 0.00,
    "Oat": 0.50,
    "Almond": 0.50
}

FLAVOR_SYRUPS = {
    "Vanilla": 0.25,
    "Caramel": 0.25,
    "Hazelnut": 0.25,
    "Peppermint": 0.25,
    "Mocha": 0.25,
    "Blackberry": 0.25,
}

COLD_FOAM = {
    "Cold Foam": 0.70,
}

#signature drinks
SIGNATURE_DRINKS = {
    "Honey Cloud Latte": {"price": 5.00, "description": "A warm latte topped with fluffy vanilla cold foam and honey drizzle."},
    "Chocolate Swirl Mocha": {"price": 5.00, "description": "Rich mocha blended with chocolate syrup and silky steamed milk."},
    "Vanilla Breeze Cold Brew": {"price": 5.00, "description": "Smooth cold brew sweetened with vanilla and topped with light cold foam."},
    "Blackberry Matcha Bloom": {"price": 5.00, "description": "Fresh matcha mixed with blackberry syrup and topped with cold foam."},
    "Matcha Mint Kiss": {"price": 5.00, "description": "Iced matcha sweetened with peppermint and layered with cool minty foam."}
}

#bakery
BAKERY = {
    "Chocolate Chip Cookie": 1.50,
    "Croissant": 2.25,
    "Blueberry Muffin": 2.75,
    "Banana Bread Slice": 2.00
}

#customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self.order_list = []
        self.total = 0.0

    def add_item(self, item_name, price):
        self.order_list.append(item_name)
        self.total += price

# ============================
#FUNCTIONS
# ============================
def intro():
    print("--------- Welcome to The Lavender LatteHouse ---------")
    print("The warm and cozy cafe where we brew your drinks to perfection")

def display_menu():
    print("======================MENU======================")
    #HOT DRINKS
    print("🔥 HOT DRINKS 🔥")
    for drink, sizes in HOT_DRINKS.items():
        print(f"  {drink}: " + ", ".join([f"{size.capitalize()} ${price:.2f}" for size, price in sizes.items()]))
    print()
    #ICED DRINKS
    print("❄️ ICED DRINKS ❄️")
    for drink, sizes in ICED_DRINKS.items():
        print(f"  {drink}: " + ", ".join([f"{size.capitalize()} ${price:.2f}" for size, price in sizes.items()]))
    print()
    #SIGNATURE DRINKS
    print("⭐ SIGNATURE DRINKS (Flat Price $5 each) ⭐")
    for drink, info in SIGNATURE_DRINKS.items():
        print(f"  {drink}: ${info['price']:.2f}")
        print(f"    → {info['description']}")
    print()
    #CUSTOMIZATIONS
    print("✨ CUSTOMIZATION OPTIONS ✨")
    print("  Milk Options:")
    for milk, cost in MILK_OPTIONS.items():
        print(f"    {milk}: +${cost:.2f}")
    print("\n  Flavor Syrups:")
    for syrup, cost in FLAVOR_SYRUPS.items():
        print(f"    {syrup}: +${cost:.2f}")
    print("\n  Cold Foam:")
    for foam, cost in COLD_FOAM.items():
        print(f"    {foam}: +${cost:.2f}")
    #BAKERY
    print("\n🍪 BAKERY 🍪")
    for item, price in BAKERY.items():
        print(f"  {item}: ${price:.2f}")
    print("\n===========================================\n")

def suggest_bakery():
    suggestion = random.choice(list(BAKERY.keys()))
    print(f"💡 Would you like to try our {suggestion}?")

def take_order():
    #gets the customers name to make it personable
    customer_name = input("Hello :) My name is Ophelia and I will be taking your order today. What's your name? ")
    customer_name = customer_name[0].upper() + customer_name[1:]
    customer = Customer(customer_name)

    print(f"\nHello {customer.name}! Type the exact name of the item you want. Type 'done' when finished.\n")

    ALL_DRINKS = {**HOT_DRINKS, **ICED_DRINKS}
    while True:
        suggest_bakery()
        choice = input("What would you like to order? ")

        if choice.lower() == "done":
            print("\nOrder Summary:")
            for item in customer.order_list:
                print(f"  - {item}")
            print(f"\nTotal: ${customer.total:.2f}")
            print(f"\nBarista: Order for {customer_name} is ready! Enjoy your day! ☕💜")
            break

        #drinks
        elif choice in ALL_DRINKS:
            size = input("Choose size (small, medium, large): ")
            if size not in ALL_DRINKS[choice]:
                print("Invalid size!")
                continue
            price = ALL_DRINKS[choice][size]
            customizations = ""

            milk = input("Choose milk (Whole, Skim, Oat, Almond): ")
            if milk in MILK_OPTIONS:
                price += MILK_OPTIONS[milk]
                customizations += ", " + milk + " milk"

            syrup = input("Add syrup? (Vanilla, Caramel, Hazelnut, Peppermint, Mocha, Blackberry or no): ")
            if syrup in FLAVOR_SYRUPS:
                price += FLAVOR_SYRUPS[syrup]
                customizations += ", " + syrup + " syrup"

            cold_foam = input("Add Cold Foam? (yes/no): ")
            if cold_foam == "yes":
                price += COLD_FOAM["Cold Foam"]
                foam_syrup = input("Choose syrup for Cold Foam or 'no': ")
                if foam_syrup in FLAVOR_SYRUPS:
                    price += FLAVOR_SYRUPS[foam_syrup]
                    customizations += ", Cold Foam with " + foam_syrup + " syrup"
                else:
                    customizations += ", Cold Foam"

            customer.add_item(f"{choice} ({size}{customizations})", price)
            print(f"{choice} added! ${price:.2f}")

        #signature drinks
        elif choice in SIGNATURE_DRINKS:
            price = SIGNATURE_DRINKS[choice]["price"]
            customizations = ""

            milk = input("Choose milk (Whole, Skim, Oat, Almond): ")
            if milk in MILK_OPTIONS:
                price += MILK_OPTIONS[milk]
                customizations += ", " + milk + " milk"

            syrup = input("Add syrup? (Vanilla, Caramel, Hazelnut, Peppermint, Mocha, Blackberry or no): ")
            if syrup in FLAVOR_SYRUPS:
                price += FLAVOR_SYRUPS[syrup]
                customizations += ", " + syrup + " syrup"

            cold_foam = input("Add Cold Foam? (yes/no): ")
            if cold_foam == "yes":
                price += COLD_FOAM["Cold Foam"]
                foam_syrup = input("Choose syrup for Cold Foam or 'no': ")
                if foam_syrup in FLAVOR_SYRUPS:
                    price += FLAVOR_SYRUPS[foam_syrup]
                    customizations += ", Cold Foam with " + foam_syrup + " syrup"
                else:
                    customizations += ", Cold Foam"

            customer.add_item(f"{choice}{customizations}", price)
            print(f"{choice} added! ${price:.2f}")

        #bakery
        elif choice in BAKERY:
            price = BAKERY[choice]
            customer.add_item(choice, price)
            print(f"{choice} added! ${price:.2f}")

        else:
            print("Item not found. Please try again.")


# ============================
intro()
display_menu()
take_order()