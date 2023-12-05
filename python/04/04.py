import re

CACHE = {}


def parse_card(card):
    match = re.match(r"Card.*\d+:", card)
    card_minus_card_num = card[match.end() :]
    split = card_minus_card_num.split("|")
    winners = [int(num.strip()) for num in split[0].strip().split(" ") if num.strip()]
    my_nums = [int(num.strip()) for num in split[1].strip().split(" ") if num.strip()]
    count = 0
    for winner in winners:
        if winner in my_nums:
            count += 1
    if count > 0:
        return 2 ** (count - 1)
    return 0


def count_winners(card):
    match = re.match(r"Card[^\d]*(\d+):", card)
    card_number = int(match.groups()[0])
    card_minus_card_num = card[match.end() :]
    split = card_minus_card_num.split("|")
    winners = [int(num.strip()) for num in split[0].strip().split(" ") if num.strip()]
    my_nums = [int(num.strip()) for num in split[1].strip().split(" ") if num.strip()]
    count = 0
    for winner in winners:
        if winner in my_nums:
            count += 1
    return card_number, count


def score_cards(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f.readlines():
            points = parse_card(line)
            print(points)
            total += points
    return total


def process_scratchcards(input_file):
    with open(input_file, "r") as f:
        cards = [line.strip() for line in f.readlines()]
    processed = []
    queue = [] + cards
    processed_num = {}
    to_process = {}
    for i in range(len(cards)):
        to_process[i + 1] = 1
    curr_num = 1
    total_processed = 0
    while curr_num <= len(cards):
        card_number, count = count_winners(cards[curr_num - 1])
        total_processed += to_process[curr_num]
        for i in range(1, count + 1):
            if curr_num + i in to_process:
                to_process[curr_num + i] += to_process[curr_num]
        curr_num += 1
    return total_processed


print(process_scratchcards("./04.in"))
