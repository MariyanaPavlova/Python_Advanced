def words_sorting(*args):

    dict = {}
    summ = 0
    all_summ = 0

    for el in args:
        if el not in dict:
            dict[el] = 0
        for i in el:
            sym = ord(i)
            summ += sym

        dict[el] = summ

        all_summ += summ
        summ = 0

    out_str = ""
    if all_summ % 2 == 0:
        dict_s = sorted(dict.items(), key=lambda x: x[0])
        for k, v in dict_s:
            out_str += (f'{k} - {v}\n')
        return out_str
    else:
        dict_s = sorted(dict.items(), key=lambda x: -x[1])
        for k, v in dict_s:
            out_str += (f'{k} - {v}\n')
        return out_str


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
print(
    words_sorting(
        'cacophony',
        'cacophony'
    ))