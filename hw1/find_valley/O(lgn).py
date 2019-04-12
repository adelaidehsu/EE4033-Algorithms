import sys
import time

in_file = sys.argv[1]
out_file = sys.argv[2]

arr = []
with open(in_file, 'r') as f:
    for line in f:
        arr.append(float(line))

def Valley(arr, h, t, size):
    m = h+ int((t-h)/2)
    if(m == 0 or arr[m-1] >= arr[m])and(m == size-1 or arr[m+1] >= arr[m]):
        return m
    elif(m > 0 and arr[m-1] <= arr[m]):
        return Valley(arr, h, m-1, size)
    else:
        return Valley(arr, m+1, t, size)

size = len(arr)
with open(out_file, 'w') as f:
    f.write(str(Valley(arr, 0, size-1, size)))