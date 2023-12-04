import re

NUMBERS = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}


def get_calibration_values(input_file):
    with open(input_file, "r") as f:
        input_strings = f.readlines()
        calibration_values = []
        for line in input_strings:
            match = re.findall(
                r"(one|two|three|four|five|six|seven|eight|nine|\d)*", line
            )
            calibration_values.append(int(NUMBERS[match[0]] + NUMBERS[match[-1]]))
    return calibration_values


def get_calibration_values_v2(input_file):
    with open(input_file, "r") as f:
        input_strings = f.readlines()
        calibration_values = []
        for line in input_strings:
            number_1 = ""
            search_string = ""
            for char in line:
                search_string += char
                if any(
                    [
                        re.search(number, search_string) != None
                        for number in NUMBERS.keys()
                    ]
                ):
                    number_1 = NUMBERS[
                        re.findall(
                            r"(one|two|three|four|five|six|seven|eight|nine|\d)",
                            search_string,
                        )[0]
                    ]
                    print(number_1)
                    break
            number_2 = ""
            search_string = ""
            for char in reversed(line):
                search_string = char + search_string
                if any(
                    [
                        re.search(number, search_string) != None
                        for number in NUMBERS.keys()
                    ]
                ):
                    number_2 = NUMBERS[
                        re.findall(
                            r"(one|two|three|four|five|six|seven|eight|nine|\d)",
                            search_string,
                        )[0]
                    ]
                    print(number_2)
                    break
            calibration_values.append(int(number_1 + number_2))
    return calibration_values


for cv in enumerate(get_calibration_values_v2("./01_2.in")):
    print(cv)

print(sum(get_calibration_values_v2("./01_2.in")))
