clothes = [int(x) for x in input().split()]
capacity = int(input())

curr_cap = capacity
used_racks = 1

while clothes:
    cur_piece = clothes[-1]

    if cur_piece <= curr_cap:
        curr_cap -= cur_piece
        clothes.pop()
    else:
        curr_cap = capacity
        used_racks += 1

print(used_racks)
