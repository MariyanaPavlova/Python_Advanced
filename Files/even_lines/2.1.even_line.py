special_symbols = ["-", ",", ".", "!", "?"]

with open("2.1.even_input.txt", "r") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = "".join(reversed(line.strip().split()))
            for i in special_symbols:
                result = result.replace(i, "@")

            print(result)
