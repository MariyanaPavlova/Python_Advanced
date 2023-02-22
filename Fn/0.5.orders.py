def calculate_total_price(prod, quant: int):
    if prod == "coffee":
        return 1.50 * quant
    elif prod == "coke":
        return 1.40 * quant
    elif prod == "water":
        return 1.00 * quant
    elif prod == "snacks":
        return 2.00 * quant


product = input()
quantity = int(input())
a = calculate_total_price(product, quantity)
print(f'{a:.2f}')




