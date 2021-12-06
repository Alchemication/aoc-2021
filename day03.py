from collections import Counter

import pandas as pd
import numpy as np

from lib import read_file

f_content = read_file("inputs/day03.txt")

# task 1
# records = [list(r) for r in f_content]
# df = pd.DataFrame(records)
# most_frequent = "".join(df.mode().values[0])  # get most frequent terms
# least_frequent = "".join(["1" if i == "0" else "0" for i in most_frequent])
#
# print("most-bin: ", most_frequent)
# print("least-bin:", least_frequent)
#
# most_frequent_int = int(most_frequent, 2)
# least_frequent_int = int(least_frequent, 2)
#
# print("most-int:", most_frequent_int, "least-int:", least_frequent_int,
#       "multiplied:", most_frequent_int*least_frequent_int)

# task2
records = np.array([[int(n) for n in list(r)] for r in f_content])
ox_records = records.copy()
co2_records = records.copy()

# figure out oxygen
for i in range(len(records[0])):
    # grab all vertical values from records at column "i"
    # check frequency and select only items starting with this value
    if len(ox_records) == 1:
        break
    records_in_col = ox_records[:, i]
    zero_count = [n for n in records_in_col if n == 0]
    one_count = [n for n in records_in_col if n == 1]
    most_freq = 0 if len(zero_count) > len(one_count) else 1
    # from remaining records, select only ones with
    # value at column "i" equal to  "most_freq"
    mask = (ox_records[:, i] == most_freq)
    ox_records = ox_records[mask, :].copy()

ox_bin = "".join([str(n) for n in ox_records[0].tolist()])
ox_int = int(ox_bin, 2)
print("ox", ox_bin, ox_int)

# figure out co2
for i in range(len(records[0])):
    # grab all vertical values from records at column "i"
    # check frequency and select only items starting with this value
    if len(co2_records) == 1:
        break
    records_in_col = co2_records[:, i]
    zero_count = [n for n in records_in_col if n == 0]
    one_count = [n for n in records_in_col if n == 1]
    least_freq = 0 if len(one_count) >= len(zero_count) else 1
    # from remaining records, select only ones with
    # value at column "i" equal to  "least_freq"
    mask = (co2_records[:, i] == least_freq)
    co2_records = co2_records[mask, :].copy()

co2_bin = "".join([str(n) for n in co2_records[0].tolist()])
co2_int = int(co2_bin, 2)
print("co2", co2_bin, co2_int)

print("final", ox_int*co2_int)
