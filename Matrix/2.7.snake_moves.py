row, col = [int(x) for x in input().split()]
text = input()

counter = 0

for i in range(row):
    pr = ""
    for j in range(col):
        pr += text[counter]

        if counter < len(text)-1:
            counter +=1
        else:
            counter = 0

    if i%2 != 0:
        pr = pr[::-1]
    print(pr)
