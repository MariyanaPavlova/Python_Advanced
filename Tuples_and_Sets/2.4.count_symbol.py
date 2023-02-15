line = input()

char_counts = {}

for i in line:
    if i not in char_counts:
        char_counts[i] = 1
    else:
        char_counts[i] += 1


for x in sorted(char_counts.items()):
    print(f'{x[0]}: {x[1]} time/s')