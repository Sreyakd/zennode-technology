
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}


product_quantities = {}
gift_wraps = {}
for product in catalog:
    quantity = int(input(f"Enter the quantity of {product}: "))
    product_quantities[product] = quantity
    gift_wrap = input(f"Wrap {product} as a gift? (yes/no): ").lower()
    gift_wraps[product] = gift_wrap == "yes"


subtotal = 0
for product, quantity in product_quantities.items():
    price = catalog[product]
    total_price = price * quantity
    subtotal += total_price


gift_wrap_fee = 0
for product, quantity in product_quantities.items():
    if gift_wraps[product]:
        gift_wrap_fee += quantity


shipping_fee = 0
total_quantity = sum(product_quantities.values())
if total_quantity > 0:
    shipping_fee = 5 * ((total_quantity - 1) // 10 + 1)


total = subtotal + gift_wrap_fee + shipping_fee


print("Product Details:")
for product, quantity in product_quantities.items():
    price = catalog[product]
    total_price = price * quantity
    print(f"{product} - Quantity: {quantity} - Total: ${total_price}")

print(f"\nSubtotal: ${subtotal}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${total}")