shop_items = {}
for _ in range(5):
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    shop_items[name] = price

print(dict(sorted(shop_items.items(), key=lambda item: item[1], reverse=True)))

# Dictionary is a collection of key and values. Based on sets.

