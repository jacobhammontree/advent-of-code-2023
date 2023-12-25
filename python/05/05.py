import re

maps = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}

seed_to_location_map = {}


def parse_seeds(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    seed_line = lines[0]
    seeds = re.findall(r"(\d+)", seed_line)
    return [int(seed) for seed in seeds]


def parse_seed_ranges(input_file):
    ranges = []
    with open(input_file, "r") as f:
        lines = f.readlines()
    seed_line = lines[0]
    seeds = re.findall(r"(\d+)", seed_line)
    for i in range(0, len(seeds), 2):
        ranges.append({"start": int(seeds[i]), "size": int(seeds[i + 1])})
    return ranges


def find_first_line(lines, search_string):
    idx = 0
    for line in lines:
        if re.match(search_string, line):
            return idx
        idx += 1
    return -1


def read_ranges(input_file, maps):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    for map in maps.keys():
        first_index = find_first_line(lines, map)
        curr_index = first_index + 1
        while curr_index < len(lines) and lines[curr_index]:
            nums = re.findall(r"(\d+)", lines[curr_index])
            dest_start = int(nums[0])
            source_start = int(nums[1])
            range_size = int(nums[2])
            maps[map].append(
                {
                    "source_start": source_start,
                    "dest_start": dest_start,
                    "range_end": source_start + range_size,
                }
            )
            curr_index += 1

    return maps


def get_source_to_dest(source_num, source_to_dest_ranges):
    dest_num = source_num
    circuit_break = False
    for r in source_to_dest_ranges:
        if source_num >= r["source_start"] and source_num < r["range_end"]:
            if "smallest_checked" not in r:
                r["smallest_checked"] = source_num
            if source_num <= r["smallest_checked"]:
                r["smallest_checked"] = source_num
                dest_num = r["dest_start"] + (source_num - r["source_start"])
            else:
                circuit_break = True
    return dest_num, circuit_break


def get_location_nums(seeds, maps):
    locations = []
    for seed in seeds:
        if seed in seed_to_location_map:
            break
        # print(f"{seed=}")
        soil_num, _ = get_source_to_dest(seed, maps["seed-to-soil"])
        # print(f"{soil_num=}")
        fertilizer_num, _ = get_source_to_dest(soil_num, maps["soil-to-fertilizer"])
        # print(f"{fertilizer_num=}")
        water_num, _ = get_source_to_dest(fertilizer_num, maps["fertilizer-to-water"])
        # print(f"{water_num=}")
        light_num, _ = get_source_to_dest(water_num, maps["water-to-light"])
        # print(f"{light_num=}")
        temperature_num, _ = get_source_to_dest(light_num, maps["light-to-temperature"])
        # print(f"{temperature_num=}")
        humidity_num, _ = get_source_to_dest(
            temperature_num, maps["temperature-to-humidity"]
        )
        # print(f"{humidity_num=}")
        location_num, _ = get_source_to_dest(humidity_num, maps["humidity-to-location"])
        # print(f"{humidity_num=}")
        locations.append(location_num)
        seed_to_location_map[seed] = location_num
    return locations


def get_location_nums_from_ranges(seed_ranges, maps):
    locations = []
    for seed_range in seed_ranges:
        print("Processing seed range")
        i = 0
        for seed in range(
            seed_range["start"], seed_range["start"] + seed_range["size"]
        ):
            i += 1
            print(i)
            if seed in seed_to_location_map:
                break
            # print(f"{seed=}")
            circuit_break = False
            soil_num, _ = get_source_to_dest(seed, maps["seed-to-soil"])
            if circuit_break:
                break
            # print(f"{soil_num=}")
            fertilizer_num, _ = get_source_to_dest(soil_num, maps["soil-to-fertilizer"])
            if circuit_break:
                break
            # print(f"{fertilizer_num=}")
            water_num, _ = get_source_to_dest(
                fertilizer_num, maps["fertilizer-to-water"]
            )
            if circuit_break:
                break
            # print(f"{water_num=}")
            light_num, _ = get_source_to_dest(water_num, maps["water-to-light"])
            if circuit_break:
                break
            # print(f"{light_num=}")
            temperature_num, _ = get_source_to_dest(
                light_num, maps["light-to-temperature"]
            )
            if circuit_break:
                break
            # print(f"{temperature_num=}")
            humidity_num, _ = get_source_to_dest(
                temperature_num, maps["temperature-to-humidity"]
            )
            if circuit_break:
                break
            # print(f"{humidity_num=}")
            location_num, _ = get_source_to_dest(
                humidity_num, maps["humidity-to-location"]
            )
            if circuit_break:
                break
            # print(f"{humidity_num=}")
            locations.append(location_num)
            seed_to_location_map[seed] = location_num
    return locations


# seeds = parse_seeds("05.in")
# maps = read_ranges("05.in", maps)
# print(min(get_location_nums(seeds, maps)))
seeds = parse_seed_ranges("05.in")
maps = read_ranges("05.in", maps)
location_nums = get_location_nums_from_ranges(seeds, maps)
print(min(location_nums))
