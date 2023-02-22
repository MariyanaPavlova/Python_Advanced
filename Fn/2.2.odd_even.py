comand = input()
nums = [int(x) for x in input().split()]

# if comand == 'Even':
#     even = [x for x in nums if x%2 == 0] * len(nums)
#     print(even)
# else:
#     odd = [x for x in nums if x%2 == 1] * len(nums)
#     print(odd)

parity = 0 if comand == 'Even' else 1

result = sum([x for x in nums if x%2 == parity]) * len(nums)
print(result)

