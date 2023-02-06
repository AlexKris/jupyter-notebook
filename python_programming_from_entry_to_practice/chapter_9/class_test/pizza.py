def make_pizza(size, *toppints):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppints:
        print(f"- {topping}")