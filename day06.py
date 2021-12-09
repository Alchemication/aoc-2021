from lib import read_file

f_content = read_file("./inputs/day06.txt", ret_raw=True)
curr_lanterns = [int(n) for n in f_content.split(",")]

# n_days = 80  # task 1
n_days = 256  # task 2
spawn_time = 6
new_lantern_time = 8

for i, _ in enumerate(range(n_days)):
    if i != 0 and i % 10 == 0:
        print(f"Processing day {i}, length of curr_lanterns: {len(curr_lanterns)} ...")
    updated_lanterns = []
    spawned_lanterns = []
    for lantern in curr_lanterns:
        if lantern == 0:
            lantern = spawn_time
            spawned_lanterns.append(new_lantern_time)
        else:
            lantern -= 1
        updated_lanterns.append(lantern)
    for lantern in spawned_lanterns:
        updated_lanterns.append(lantern)
    curr_lanterns = updated_lanterns

print("Done")
print(len(curr_lanterns))
