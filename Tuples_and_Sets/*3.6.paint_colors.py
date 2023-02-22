from collections import deque

colors = {"red", "yellow", "blue", "orange", "purple", "green"}

substring = deque(input().split())
collected_colors = []

while substring:
    first_substr = substring.popleft()
    second_substr = substring.pop() if substring else ""

    result = first_substr + second_substr
    if result in colors:
        collected_colors.append(result)
        continue

    result = second_substr + first_substr
    if result in colors:
        collected_colors.append(result)
        continue

    first_substr = first_substr[:-1]
    second_substr = second_substr[:-1]

    if first_substr:
        substring.insert(len(substring) //2, first_substr)
    if second_substr:
        substring.insert(len(substring) //2, second_substr)

result_l = []
secondary_colors_map = {
    'orange': ['red', 'yellow'],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"],
}

for i in collected_colors:
    if i not in secondary_colors_map:
        result_l.append(i)
    else:
        is_valid = True
        for j in secondary_colors_map[i]:
            if j not in collected_colors:
                is_valid = False
                break
        if is_valid:
            result_l.append(i)

print(result_l)