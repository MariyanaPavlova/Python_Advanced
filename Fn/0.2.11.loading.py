def loading_bar(num):
    n_10 = num/10
    list = []

    for i in range(1, 10+1):
        if i <= n_10:
            list.append('%')
        else:
            list.append('.')

    if num < 100:
        print(f'{n}% [{"".join(list)}]')
        print(f'Still loading...')
    if num == 100:
        print(f'{n}% Complete!')
        print(f'[{"".join(list)}]')


n = int(input())
loading_bar(n)