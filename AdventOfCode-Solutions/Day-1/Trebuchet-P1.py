with open('Lines.txt') as file:
    lines = file.readlines()

finalnumber = 0;

for line in lines:
    line = line.strip()

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