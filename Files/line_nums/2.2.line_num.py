import re
from string import punctuation

with open("2.2.input.txt", "r") as input_file, open("2.2.output.txt", "w") as output_file:
    for row, line in enumerate(input_file):
        stripped_line = line.strip()
        leters_count = len(re.findall('[a-zA-Z]', stripped_line))
        marks_count = len(re.findall("[,.\-\"':?!]", stripped_line))
        output_file.write(f'Line {row+1}: {stripped_line} ({leters_count})({marks_count})\n')

