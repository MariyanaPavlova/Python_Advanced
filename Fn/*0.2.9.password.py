def chech_valid_passord(word):
    is_valid = True
    consist_let_dig = True
    count_digits = 0


    if len(word) < 6 or len(word) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False

    for i in word:
        if i.isdigit():
          count_digits +=1

    if not word.isalnum():
      is_valid = False
      print('Password must consist only of letters and digits')

    if count_digits < 2:
      is_valid = False
      print('Password must have at least 2 digits')

    return is_valid


password = input()
result = chech_valid_passord(password)

if result:
  print("Password is valid")