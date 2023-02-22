def fill_the_box(height, lenght, width, *args):
    box = height * lenght * width

    free_space = box
    left_cubes = 0

    for el in args:
        if el == 'Finish':
            break

        if free_space - el > 0:
            free_space -= el
        else:
            left_cubes += el -free_space
            free_space = 0

    if free_space == 0:
        return (f'No more free space! You have {left_cubes} more cubes.')
    else:
        return (f'There is free space in the box. You could put {free_space} more cubes.')

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5,"Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))