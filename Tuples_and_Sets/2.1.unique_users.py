n = int(input())

usernames = set()

for i in range(n):
    user = input()
    usernames.add(user)

#print("\n".join(usernames))

print(*usernames, sep='\n')