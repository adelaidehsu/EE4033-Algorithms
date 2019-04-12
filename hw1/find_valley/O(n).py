import sys
import time

in_file = sys.argv[1]
out_file = sys.argv[2]

array = []
array.append(float("inf"))
with open(in_file, 'r') as f:
    for line in f:
        array.append(float(line))
array.append(float("inf"))

valley = float("inf")
for i in range(1, len(array)-1):
    if(array[i-1] >= array[i] and array[i+1] >= array[i]):
        valley = i-1
        break

with open(out_file, 'w') as f:
    f.write(str(valley))