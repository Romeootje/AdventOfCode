with open('Cards.txt') as file:
    lines = file.readlines()

cards = [line.strip() for line in lines]
total_cards = len(cards)

def count_winning_numbers(winningnumbers, card):
    winningnumbers_set = set(winningnumbers.strip().split())
    card_set = set(card.strip().split())
    return len(winningnumbers_set.intersection(card_set))

card_copies = [1] * total_cards 

for i in range(total_cards):
    card = cards[i].split("|")
    winningnumbers = card[0]
    numbers = card[1]
    matches = count_winning_numbers(winningnumbers, numbers)

    for j in range(i + 1, min(i + 1 + matches, total_cards)):
        card_copies[j] += card_copies[i]

print(f"Total scratchcards: {sum(card_copies)}")
