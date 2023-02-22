nums = [int(x) for x in input().split()]

positive = sum([x for x in nums if x > 0])
negative = sum([x for x in nums if x < 0])

print(negative)
print(positive)

if abs(negative) > positive:
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')


---------
def calculate_strong_sum(nums):
    pos_sum = sum(filter(lambda x: x>0, nums))
    neg_sum = sum(filter(lambda x: x<0, nums))

    print(pos_sum, neg_sum, sep="\n")

    if pos_sum > abs(neg_sum):
        return f'The positives are stronger than the negatives'
    return f'The negatives are stronger than the positives' # няма нужда от ЕLSE

numbers = list(map(int, input().split()))
calculate_strong_sum(numbers)

#return приключва действието на функцията