text = 'ILovePython'

vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)

print([x for x in text if x not in vowels])
