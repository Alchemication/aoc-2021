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
bingo_boards = bingo_boards[:2]  # TODO: Remove debug !!!
bingo_boards = np.array(bingo_boards)

#print(bingo_boards)

# initialize grid with zeros, which we will use to mark numbers (as 1)
answer_boards = np.zeros(shape=(len(bingo_boards), 5, 5), dtype=int)

# run through random numbers:
# search for number across the boards, and keep indexes
# populate 1's on the mask for selected indexes
# find consecutive rows or columns with 1's - if found stop here,
# find the first board with the 5 consecutive 1's
# sum up all values in that board where mask-values are 0

last_no = None
last_idx = None

for i, curr_no in enumerate(rand_numbers):
    # create a mask for indexes where number was found
    mask = bingo_boards[:, :, :] == curr_no
    # populate answers
    answer_boards[mask] = 1
    # search all boards and find the first one which has 5 ones
    # across all cols or rows
    for b in answer_boards:
        col_sum = np.sum(b, axis=(0,))
        row_sum = np.sum(b, axis=(1,))


    # sum values across columns
    # col_sum = np.sum(answer_boards, axis=(1,))
    # # count number of occurrences for 5
    # unique, counts = np.unique(col_sum, return_counts=True)
    # counts_dict = dict(zip(unique, counts))


# print("last no", last_no, "last idx", last_idx, "multiply",
#       last_no * sum(rand_numbers[last_idx+1:]))

my_arr = np.array(
    [
        [0, 1],
        [0, 1]
    ]
)
print(my_arr)
print("COLS:")
print(np.sum(my_arr, axis=(0,)))
print("ROWS:")
print(np.sum(my_arr, axis=(1,)))
