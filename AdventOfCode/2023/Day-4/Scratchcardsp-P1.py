with open('Cards.txt') as file:
    lines = file.readlines()

totalwin = 0

for line in lines:
    game, parts = line.split(":")
    winningnumbers, card = parts.split("|")

    winningnumbers_set = set(winningnumbers.strip().split())
    card_set = set(card.strip().split())
    winninggames = winningnumbers_set.intersection(card_set)

    count_winning_numbers = len(winninggames)

    if count_winning_numbers > 0:
        calc_winning = 2 ** (count_winning_numbers - 1)
    else:
        calc_winning = 0

    totalwin += calc_winning

    print(f"Calculated: {totalwin}")

