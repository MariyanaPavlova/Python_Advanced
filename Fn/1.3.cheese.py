def sorting_cheeses(**kwargs):

    sort_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for name, qunt in sort_cheese:
        result += name + "\n"
        sorted_qunt = sorted(qunt, reverse=True)
        result += '\n'.join([str(x) for x in sorted_qunt]) + '\n'

    return result

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)