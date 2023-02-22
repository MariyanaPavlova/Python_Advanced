def numbers_searching(*args):

    min_n = min(args)
    max_n = max(args)

    clear_args = set(args)

    missing_elements = ''

    for el in range(min_n, max_n +1):
        if el not in clear_args:
            missing_elements = el
            break

    args_l = list(args)
    dupl = []

    while args_l:
        a = args_l.pop()
        if a in args_l:
            dupl.append(a)

    dupl_s = sorted(list(dict.fromkeys(dupl)))

    return [missing_elements, dupl_s]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
