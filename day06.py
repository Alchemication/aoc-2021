from lib import read_file

f_content = read_file("./inputs/day06.txt", ret_raw=True)
curr_lanterns = [int(n) for n in f_content.split(",")]

# Note: Solution copied from helper Reddit page for aoc'21,
# part 1 was almost too easy, but could not figure out part 2 :-(
# The solution below is simply speaking brilliant ;)


def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    # print(tracker)
    for day in range(days):
        # print(" ** day:", day, " ** (day + 7) % 9:", (day + 7) % 9, " ** day % 9:", day % 9)
        tracker[(day + 7) % 9] += tracker[day % 9]
        # print("day:", day, "tracker:", tracker)
    return sum(tracker)


print(f"Part 1: {solve(curr_lanterns, 80)}")
print(f"Part 2: {solve(curr_lanterns, 256)}")
