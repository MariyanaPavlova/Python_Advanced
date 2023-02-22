def list_manipulator(listt, do, done, *k):

    # if do == 'add' and done == "beginning":  #може с функция
    #     if k:
    #         for el, i in enumerate(k):
    #             listt.insert(el, i)
    # elif do == "add" and done == 'end':
    #     if k:
    #         for el in k:
    #             listt.append(el)
    #
    # if do == 'remove' and done == "beginning":  #може с функция
    #     if k:
    #         countt = k[0]
    #         for i in range(countt):
    #             listt.pop(0)
    #     else:
    #         listt.pop(0)

    # elif do == "remove" and done == 'end':
    #     if k:
    #         countt = k[0]
    #         for i in range(countt):
    #             listt.pop(-1)
    #     else:
    #         listt.pop(-1)
    #
    # add_things(listt, do, done, *k)
    # remove_things(listt, do, done, *k)
    #
    # return listt

def add_things(lis, d, don, *kk):
    if d == 'add' and don == "beginning":
        if kk:
            for el, i in enumerate(kk):
                lis.insert(el, i)
            return lis
    elif d == "add" and don == 'end':
        if kk:
            for el in kk:
                lis.append(el)
            return lis

def remove_things(listtt, doo, donee, *kkk):
    if doo == 'remove' and donee == "beginning":
        if kkk:
            countt = kkk[0]
            for i in range(countt):
                listtt.pop(0)
        else:
            listtt.pop(0)
        return listtt

    elif doo == "remove" and donee == 'end':
        if kkk:
            countt = kkk[0]
            for i in range(countt):
                listtt.pop(-1)
        else:
            listtt.pop(-1)
        return listtt

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))