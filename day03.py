import pandas as pd

from lib import read_file

f_content = read_file("inputs/day03.txt")

# task 1
records = [list(r) for r in f_content]
df = pd.DataFrame(records)
most_frequent = "".join(df.mode().values[0])  # get most frequent terms
least_frequent = "".join(["1" if i == "0" else "0" for i in most_frequent])

print("most-bin: ", most_frequent)
print("least-bin:", least_frequent)

most_frequent_int = int(most_frequent, 2)
least_frequent_int = int(least_frequent, 2)

print("most-int:", most_frequent_int, "least-int:", least_frequent_int,
      "multiplied:", most_frequent_int*least_frequent_int)
