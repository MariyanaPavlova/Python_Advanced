def stock_availability(boxes, do, *k):

    if do == 'delivery':
        for el in k:
            boxes.append(el)
    if do == 'sell':
        if k:
            for i in k:
                if type(i) == int:
                    for z in range(i):
                        if z <= i:
                            boxes.pop(0)

                else:
                    if i in boxes:
                        boxes = list(filter((i).__ne__, boxes))
        else:
            boxes.pop(0)

    return boxes

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
print(stock_availability(["chocolate", "vanilla", "banana","choco"], "sell", 3))
