def start_spring(**kwargs):
    type_dict = {}

    for k, v in kwargs.items():
        if v not in type_dict:
            type_dict[v] = [k]
        else:
            type_dict[v].append(k)

    type_dict_s = sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    out_str = ""

    for k, v in type_dict_s:
        out_str += (f'{k}:\n')
        for i in sorted(v):
            out_str += (f'-{i}\n')

    return out_str

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
