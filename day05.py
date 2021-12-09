import numpy as np

from lib import read_file

f_content = read_file("inputs/day05.txt")

# task 1
# process_records = []
#
# # process raw data
# for r in f_content:
#     start, end = r.split("->")
#     x1, y1 = start.split(",")
#     x2, y2 = end.split(",")
#     x1, y1 = int(x1.strip()), int(y1.strip())
#     x2, y2 = int(x2.strip()), int(y2.strip())
#     if x1 == x2 or y1 == y2:
#         process_records.append([(x1, y1), (x2, y2)])
#
# # create a 2D plane based on the max coordinates
# diagram = np.zeros((np.max(process_records) + 1, np.max(process_records) + 1))
#
# points = []
# for r in process_records:
#     (x1, y1), (x2, y2) = r
#     # horizontal lines
#     if y1 == y2:
#         if x1 < x2:
#             for p in range(x1, x2 + 1):
#                 points.append((p, y1))
#         elif x1 > x2:
#             for p in range(x2, x1 + 1):
#                 points.append((p, y1))
#         else:
#             raise ValueError("fix me please - 1")
#     # vertical lines
#     if x1 == x2:
#         if y1 < y2:
#             for p in range(y1, y2 + 1):
#                 points.append((x1, p))
#         elif y1 > y2:
#             for p in range(y2, y1 + 1):
#                 points.append((x1, p))
#         else:
#             raise ValueError("fix me please - 2")
#
# for x, y in points:
#     diagram[y][x] += 1  # flip coordinates to match the output in the online example
#
# mask = (diagram > 1)
# high_overlap_count = mask.astype(int).sum()
#
# print("high_overlap_count:", high_overlap_count)

# task 2

process_records = []

# process raw data
for r in f_content:
    start, end = r.split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    x1, y1 = int(x1.strip()), int(y1.strip())
    x2, y2 = int(x2.strip()), int(y2.strip())
    process_records.append([(x1, y1), (x2, y2)])

# create a 2D plane based on the max coordinates
diagram = np.zeros((np.max(process_records) + 1, np.max(process_records) + 1))

points = []
for r in process_records:
    (x1, y1), (x2, y2) = r
    # horizontal lines
    if y1 == y2:
        if x1 < x2:
            for p in range(x1, x2 + 1):
                points.append((p, y1))
        elif x1 > x2:
            for p in range(x2, x1 + 1):
                points.append((p, y1))
        else:
            raise ValueError("fix me please - 1")
    # vertical lines
    elif x1 == x2:
        if y1 < y2:
            for p in range(y1, y2 + 1):
                points.append((x1, p))
        elif y1 > y2:
            for p in range(y2, y1 + 1):
                points.append((x1, p))
        else:
            raise ValueError("fix me please - 2")
    # diagonal lines
    else:
        x, y = [], []
        # figure out x
        if x1 < x2:
            for p in range(x1, x2 + 1):
                x.append(p)
        elif x1 > x2:
            for p in range(x1, x2 - 1, -1):
                x.append(p)
            # print("x:", x1, x2, x)
        else:
            raise ValueError("fix me please - 3")

        # figure out y
        if y1 < y2:
            for p in range(y1, y2 + 1):
                y.append(p)
        elif y1 > y2:
            for p in range(y1, y2 - 1, -1):
                y.append(p)
        else:
            raise ValueError("fix me please - 4")
        for p in list(zip(x, y)):
            points.append(p)

for x, y in points:
    diagram[y][x] += 1  # flip coordinates to match the output in the online example

print(diagram)

mask = (diagram > 1)
high_overlap_count = mask.astype(int).sum()

print("high_overlap_count:", high_overlap_count)
