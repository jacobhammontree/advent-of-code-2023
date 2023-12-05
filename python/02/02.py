import re

MAXES = {"red": 12, "green": 13, "blue": 14}


def parse_game(input_file):
    total = 0
    total_power = 0
    with open(input_file, "r") as f:
        raw_games = f.readlines()
        for game in raw_games:
            game_maxes = {"red": 0, "green": 0, "blue": 0}
            print(game)
            m = re.match(r"Game (\d+): ", game)
            game_number = int(m.group(1))
            turns = [s.strip() for s in game[m.end() :].strip().split(";")]
            turns = [t.split(",") for t in turns]
            good_turns = 0
            for turn in turns:
                good_pulls = 0
                for pull in turn:
                    match = re.match(r"(\d+) (.*)", pull.strip())
                    color = match.groups()[1]
                    number = int(match.groups()[0])
                    if int(number) <= MAXES[color]:
                        good_pulls += 1
                    if game_maxes[color] < number:
                        game_maxes[color] = number
                if good_pulls == len(turn):
                    good_turns += 1
            if good_turns == len(turns):
                total += game_number
            game_power = game_maxes["red"] * game_maxes["green"] * game_maxes["blue"]
            total_power += game_power
    return total, total_power


print(parse_game("./02_1.in"))
