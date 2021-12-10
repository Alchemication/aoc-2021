from lib import read_file

f_content = read_file("./inputs/day07.txt", ret_raw=True)
positions = [int(n) for n in f_content.split(",")]


# task 1

# def solve(pos):
#     min_fuel_pos = None
#     min_fuel_val = None
#     all_solutions = {}
#
#     for i in range(max(pos) + 1):
#         curr_fuel_val = 0
#         for p in pos:
#             curr_fuel_val += abs(p - i)
#         all_solutions[i] = curr_fuel_val
#         if min_fuel_val is None or curr_fuel_val < min_fuel_val:
#             min_fuel_val = curr_fuel_val
#             min_fuel_pos = i
#     return min_fuel_pos, min_fuel_val, all_solutions
#
#
# print(solve(positions)[:2])

# task 2

def solve(pos):
    min_fuel_pos = None
    min_fuel_val = None
    # all_solutions = {}

    for i in range(max(pos) + 1):
        if i != 0 and i % 50 == 0:
            print(f"Solving for {i} out of {max(pos)}...")
        curr_fuel_val = 0
        for p in pos:
            p_cost = 0
            for j in range(abs(p - i)):
                p_cost += j + 1
            curr_fuel_val += p_cost
            # print(p, i, curr_fuel_val, p_cost)
        # all_solutions[i] = curr_fuel_val
        if min_fuel_val is None or curr_fuel_val < min_fuel_val:
            min_fuel_val = curr_fuel_val
            min_fuel_pos = i
    return min_fuel_pos, min_fuel_val


print(solve(positions)[:2])
