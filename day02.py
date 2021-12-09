from lib import read_file

f_content = read_file("inputs/day02-input.txt")

# task 1
# hor = 0
# depth = 0
#
# for cur_dir in f_content:
#     action, steps = cur_dir.split(" ")
#     steps = int(steps)
#     if action == "forward":
#         hor += steps
#         continue
#     if action == "up":
#         depth -= steps
#         continue
#     if action == "down":
#         depth += steps
#         continue
#     raise ValueError(f"fUnexpected action: {action}")
#
# print("hor", hor, "depth", depth, "res", hor*depth)

# task 2

aim = 0
hor = 0
depth = 0

for cur_dir in f_content:
    action, steps = cur_dir.split(" ")
    steps = int(steps)
    # down adds to aim
    # up decreases from aim
    # forward adds to horizontal and adds (cur_aim * forward) to depth
    if action == "forward":
        hor += steps
        depth += steps * aim
        continue
    if action == "up":
        aim -= steps
        continue
    if action == "down":
        aim += steps
        continue
    raise ValueError(f"fUnexpected action: {action}")

print("hor", hor, "depth", depth, "res", hor*depth)
