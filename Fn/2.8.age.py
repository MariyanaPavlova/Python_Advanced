def age_assignment(*args, **kwargs):
    result = {}
    for i in args:  #i - Peter, George
        first_let = i[0]
        age = kwargs[first_let]
        result[i] = age
    return result


print(age_assignment("Peter", "George", G=26, P=19))
#
# ---------
# def age_assignment(*args, **kwargs):
#     result = {}
#
#     for fist_let, age in kwargs.items():
#        for name in args:
#             if name.startswith(fist_let):
#                 result[name] = age
#     return result
#
#
# print(age_assignment("Peter", "George", G=26, P=19