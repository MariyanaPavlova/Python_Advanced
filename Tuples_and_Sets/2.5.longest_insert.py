def gen_seq(range_i):
    start, end = [int(x) for x in range_i.split(",")]
    return set(range(start, end+1))


n = int(input())

intersect = set()

for i in range(n):
    line = input().split('-')
    fist_set = gen_seq(line[0])
    second_set = gen_seq(line[1])
    cur_intersect = fist_set.intersection(second_set)

    if len(cur_intersect) > len(intersect):
        intersect = cur_intersect

print(f'Longest intersection is [{", ".join(str(x) for x in intersect)}] with length {len(intersect)}')
