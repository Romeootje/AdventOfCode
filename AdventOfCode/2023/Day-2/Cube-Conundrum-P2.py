with open('List.txt') as file:
    lines = file.readlines()

gametotal = 0
power_total = 0

for line in lines:
    line = line.strip()
    game_number, rounds_str = line.split(':', 1)
    rounds = rounds_str.split(';')

    max_red, max_green, max_blue = 0, 0, 0
    min_red, min_green, min_blue = 0, 0, 0

    for round in rounds:
        red_dice, green_dice, blue_dice = 0, 0, 0
        dices = round.strip().split(',')

        for dice in dices:
            parts = dice.strip().split()
            if len(parts) != 2:
                continue
            count, dice_color = parts
            count = int(count)

            if dice_color == 'red':
                red_dice += count
            elif dice_color == 'green':
                green_dice += count
            elif dice_color == 'blue':
                blue_dice += count

        max_red = max(max_red, red_dice)
        max_green = max(max_green, green_dice)
        max_blue = max(max_blue, blue_dice)

        min_red = max(min_red, red_dice)
        min_green = max(min_green, green_dice)
        min_blue = max(min_blue, blue_dice)

    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        game_id = int(game_number.split()[1])
        gametotal += game_id

    power = min_red * min_green * min_blue
    power_total += power

print(f'Sum of valid game IDs: {gametotal}')
print(f'Sum of the power of the minimum set of cubes: {power_total}')
