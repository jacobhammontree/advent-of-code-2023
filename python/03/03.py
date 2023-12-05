import re

visited = []


def get_engine_schematic(input_file):
    with open(input_file, "r") as f:
        schematic = [line.strip() for line in f.readlines()]
    return schematic


def get_full_number(schematic, y, x):
    if (y, x) in visited:
        return ""
    num = schematic[y][x]
    visited.append((y, x))
    current_x = x + 1
    while (
        m := re.match(r"\d+", schematic[y][current_x]) and (y, current_x) not in visited
    ):
        visited.append((y, current_x))
        num += schematic[y][current_x]
        current_x += 1
        if not coords_in_bounds(y, current_x, schematic):
            break

    current_x = x - 1
    while (
        m := re.match(r"\d+", schematic[y][current_x]) and (y, current_x) not in visited
    ):
        visited.append((y, current_x))
        num = schematic[y][current_x] + num
        current_x -= 1
        if not coords_in_bounds(y, current_x, schematic):
            break

    return int(num)


def coords_in_bounds(y, x, schematic):
    return y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[y])


def get_adjacent_numbers(schematic, y, x):
    nums = []
    if coords_in_bounds(y - 1, x - 1, schematic) and re.match(
        r"\d+", schematic[y - 1][x - 1]
    ):
        nums.append(get_full_number(schematic, y - 1, x - 1))
    if coords_in_bounds(y - 1, x, schematic) and re.match(r"\d+", schematic[y - 1][x]):
        nums.append(get_full_number(schematic, y - 1, x))
    if coords_in_bounds(y - 1, x + 1, schematic) and re.match(
        r"\d+", schematic[y - 1][x + 1]
    ):
        nums.append(get_full_number(schematic, y - 1, x + 1))
    if coords_in_bounds(y, x - 1, schematic) and re.match(r"\d+", schematic[y][x - 1]):
        nums.append(get_full_number(schematic, y, x - 1))
    if coords_in_bounds(y, x + 1, schematic) and re.match(r"\d+", schematic[y][x + 1]):
        nums.append(get_full_number(schematic, y, x + 1))
    if coords_in_bounds(y + 1, x - 1, schematic) and re.match(
        r"\d+", schematic[y + 1][x - 1]
    ):
        nums.append(get_full_number(schematic, y + 1, x - 1))
    if coords_in_bounds(y + 1, x, schematic) and re.match(r"\d+", schematic[y + 1][x]):
        nums.append(get_full_number(schematic, y + 1, x))
    if coords_in_bounds(y + 1, x + 1, schematic) and re.match(
        r"\d+", schematic[y + 1][x + 1]
    ):
        nums.append(get_full_number(schematic, y + 1, x + 1))

    return [num for num in nums if num]


def get_parts_numbers_total(schematic):
    total = 0
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if re.match(r"[^\d.]", schematic[y][x]):
                total += sum(get_adjacent_numbers(schematic, y, x))
    return total


def get_gear_ratio_sum(schematic):
    total = 0
    for y in range(len(schematic)):
        for x in range(len(schematic[y])):
            if schematic[y][x] == "*":
                adjacent_numbers = get_adjacent_numbers(schematic, y, x)
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]
    return total


schematic = get_engine_schematic("./03.in")

# print(schematic[78][58])
# print(get_adjacent_numbers(schematic, 39, 61))
print(get_gear_ratio_sum(schematic))
