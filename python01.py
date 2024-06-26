# 定义产品和价格
products = {
    "apple": 1.0,
    "banana": 0.5,
    "orange": 0.75
}

# 打印可供选择的产品
print("Available products and their prices:")
for product, price in products.items():
    print(f"{product.capitalize()}: ${price:.2f} each")

# 初始化总价
total_price = 0

# 询问用户选择的产品和数量
while True:
    product = input("Enter the product you want to buy (or type 'done' to finish): ").lower()
    if product == 'done':
        break
    elif product in products:
        quantity = int(input(f"How many {product}s would you like to buy? "))
        total_price += products[product] * quantity
    else:
        print("Product not available. Please select a product from the list.")

# 打印报价单
print("\nQuotation:")
print("--------------------------")
print(f"Total price: ${total_price:.2f}")
print("Thank you for your purchase!")


