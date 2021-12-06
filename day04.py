import numpy as np

from lib import read_file

f_content = read_file("inputs/day04.txt", ret_raw=True)

rand_numbers = []
bingo_boards = []
curr_board = []

# read inputs (read random numbers and construct the boards)
for i, row in enumerate(f_content.split("\n")):
    if i == 0:
        rand_numbers = [int(n) for n in row.split(",")]
        continue
    if row != "" and len(curr_board) < 5:
        curr_board.append([int(n) for n in row.strip().split(" ") if n != ""])
        continue
    if len(curr_board) > 0:
        bingo_boards.append(curr_board)
        curr_board = []

# cast to np so we can work with arrays easier
bingo_boards = np.array(bingo_boards)

# initialize grid with zeros, which we will use to mark numbers (as 1)
answer_boards = np.zeros(shape=(len(bingo_boards), 5, 5), dtype=int)

# task 1

# run through random numbers:
# search for number across the boards, and keep indexes
# populate 1's on the mask for selected indexes
# find consecutive rows or columns with 1's - if found stop here,
# find the first board with the 5 consecutive 1's
# sum up all values in that board where mask-values are 0

# last_no = None
# last_idx = None
# is_win = False
# winning_board = None
# winning_board_idx = 0
#
# for i, curr_no in enumerate(rand_numbers):
#     # create a mask for indexes where number was found
#     mask = bingo_boards[:, :, :] == curr_no
#     # populate answers
#     answer_boards[mask] = 1
#     # search all boards and find the first one which has 5 ones
#     # across all cols or rows
#     for j, b in enumerate(answer_boards):
#         col_sum = np.sum(b, axis=(0,))
#         row_sum = np.sum(b, axis=(1,))
#         if 5 in col_sum or 5 in row_sum:
#             is_win = True
#             last_no = curr_no
#             winning_board_idx = j
#     if is_win:
#         break
#
# # make sure index was found
# assert winning_board_idx != 0
#
# # create a mask for unmarked numbers in winning board
# winning_board = answer_boards[winning_board_idx]
# unmarked_board_mask = (winning_board == 0)
#
# # sum all unmarked numbers in the standard board
# sum_unmarked = np.sum(bingo_boards[winning_board_idx][unmarked_board_mask])
#
# print("last number", last_no)
# print("winning_board")
# print(winning_board)
# print("unmarked mask")
# print(unmarked_board_mask)
# print("sum unmarked", sum_unmarked)
#
#
# print("final score", last_no*sum_unmarked)

# task 2

# run through random numbers:
# search for number across the boards, and keep indexes
# populate 1's on the mask for selected indexes
# find consecutive rows or columns with 1's - if found mark board as already won,
# then keep going until we find the last winning board

last_no = None
last_idx = None
is_win = False
winning_board = None
winning_board_idx = 0

winning_boards_indexes = []

for i, curr_no in enumerate(rand_numbers):
    # create a mask for indexes where number was found
    mask = bingo_boards[:, :, :] == curr_no
    # populate answers
    answer_boards[mask] = 1
    # search all boards and find the first one which has 5 ones
    # across all cols or rows
    for j, b in enumerate(answer_boards):
        if j in winning_boards_indexes:
            continue
        col_sum = np.sum(b, axis=(0,))
        row_sum = np.sum(b, axis=(1,))
        if 5 in col_sum or 5 in row_sum:
            is_win = True
            last_no = curr_no
            winning_board_idx = j
            winning_board = b.copy()
            winning_boards_indexes.append(j)

# make sure index was found
assert winning_board_idx != 0

# create a mask for unmarked numbers in winning board
unmarked_board_mask = (winning_board == 0)

# sum all unmarked numbers in the standard board
sum_unmarked = np.sum(bingo_boards[winning_board_idx][unmarked_board_mask])

print("winning_board_idx", winning_board_idx)
print("last number", last_no)
print("winning_board")
print(winning_board)
print("unmarked mask")
print(unmarked_board_mask)
print("sum unmarked", sum_unmarked)

print("final score", last_no*sum_unmarked)
