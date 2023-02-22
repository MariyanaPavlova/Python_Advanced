def inters(rang: str):
    r_one, r_two = rang.split('-')
    start, end = r_one.split(',')
    first = set()
    for z in range(int(start), int(end)+1):
        first.add(z)
    r_one, r_two = rang.split('-')
    start, end = r_two.split(',')
    second = set()
    for j in range(int(start), int(end)+1):
        second.add(j)
    return first & second


n = int(input())
result = set()

for i in range(n):

    m = inters(input())
    if len(m) > len(result):
        result = m

print(f'Longest intersection is [{", ".join(str(x) for x in result)}] with length {len(result)}')