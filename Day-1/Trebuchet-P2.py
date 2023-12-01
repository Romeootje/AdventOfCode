with open('Lines.txt') as file:
    lines = file.readlines()

number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

finalnumber = 0;
for line in lines:

    line = line.strip()

    for word, digit in number_words.items():
        line = line.replace(word, f"{word[0]}{digit}{word[-1]}")    

    for char in line:
        if char.isdigit():
            first_number = char
            break

    reversing_line = line[::-1]

    for char in reversing_line:
        if char.isdigit():
            last_number = char
            break
    
    number = int(first_number + last_number)
    finalnumber += number

print(finalnumber)