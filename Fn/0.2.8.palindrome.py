def palindrome(txt):
    if i == i[::-1]:
        return True
    return False

text = input().split(", ")
for i in text:
    print(palindrome(text))
