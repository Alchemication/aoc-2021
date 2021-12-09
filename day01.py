from lib import read_file

f_content = read_file("inputs/day01-input1.txt")

# task 1
# increased_count = 0
# prev_n = None
# for n in f_content:
#     if prev_n is not None and int(n) > prev_n:
#         increased_count += 1
#     prev_n = int(n)
#
# print(increased_count)

# task 2
increased_count = 0
prev_sum, cur_sum = None, None

f_content = [int(n) for n in f_content]

for i, n in enumerate(f_content):
    mov_window = f_content[i:i + 3]
    cur_sum = sum(mov_window)
    # break loop at the end when we don't have enough items to compare
    if len(mov_window) < 3:
        break
    if prev_sum is not None and cur_sum > prev_sum:
        increased_count += 1
    prev_sum = cur_sum

print(increased_count)
