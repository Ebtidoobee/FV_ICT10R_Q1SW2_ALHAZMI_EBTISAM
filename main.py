# ICT 10 Seatwork #2 
# Declaring Variables and Identifying Data Types
# 10-R
# Author: Ebtisam Al Hazmi


# VARIABLES & DATA TYPES

restaurant_name = "Duo Brew"                         # String
owner_name = "Ebtisam Al Hazmi"                     # String
year_established = 2025                              # Integer
has_delivery = True                                  # Boolean
business_hours = "11:00 AM - 10:00 PM"               # String
menu_prices = {                                      # Dictionary
    "Spaghetti Carbonara": 79.99,
    "Garlic Bread": 50.00,
    "Caesar Salad": 150.00,
    "Iced Tea": 30.00,
    "Sparkling Water": 20.00
}
tax_rate = 0.08                                      # Float (decimal)
common_allergens = ["Dairy", "Gluten", "Seafood"]    # List


# COLORS (ANSI escape codes)

RED = "\033[91m"
PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


# OUTPUT

print(RED + "=" * 60 + RESET)
print(PINK + BOLD + f"{restaurant_name.center(60)}" + RESET)
print(f"{'Owner: ' + owner_name:^60}")
print(f"{'Since ' + str(year_established):^60}")
print(RED + "=" * 60 + RESET)

# Menu Pricelist
print(BOLD + "\nMenu Pricelist\n" + RESET)
print(f"{'Product Name':<40}{'Price (₱)':>15}")
print("-" * 55)
for item, price in menu_prices.items():
    print(f"{item:<40}₱{price:>10.2f}")

# Business Hours
print("\n" + "-" * 55)
print(f"🕒 Open: {business_hours}")

# Delivery Status
print(f"Dine-in Available: {has_delivery}")

