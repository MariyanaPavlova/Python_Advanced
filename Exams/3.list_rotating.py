from collections import deque
def best_list_pureness(args, k):

    k = k+1
    best_sum = -1
    rot = -1
    best_rot = 0
    sum = 0
    while k:
        for i, v in enumerate(args):
            sum += i*v
        rot += 1
        if sum > best_sum:
            best_sum = sum
            best_rot = rot

        args.insert(0, args.pop())
        k -= 1
        sum =0

    return(f'Best pureness {best_sum} after {best_rot} rotations')

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)