import re

def write_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


def get_flle_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-zA-Z']+", text.lower())

path_to_words = "words.txt"
path_to_text = "text.txt"

first_file = get_flle_content(path_to_words)
second_file = get_flle_content(path_to_text)

analyze = {}

for word in first_file:
    if word in second_file:
        analyze[word] = second_file.count(word)

result = [f"{el[0]} - {el[1]}"for el in sorted(analyze.items(), key = lambda x: -x[1])]
print(result)

write_result(result)