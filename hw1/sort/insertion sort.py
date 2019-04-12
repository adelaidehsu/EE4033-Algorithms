from tools import Parser
import sys
import time

in_file = sys.argv[1]
out_file = sys.argv[2]
myParser = Parser(in_file)
P_lst = myParser.queryList()
size = len(P_lst)

def larger(str1, str2):
    asc_lst_1 = [ord(x) for x in str1]
    asc_lst_2 = [ord(x) for x in str2]
    if(len(asc_lst_1) < len(asc_lst_2)):
        for idx in range(len(asc_lst_1)):
            if asc_lst_1[idx] < asc_lst_2[idx]:
                return False
            elif asc_lst_1[idx] > asc_lst_2[idx]:
                return True
            else:
                continue
        return False
    else:
        for idx in range(len(asc_lst_2)):
            if asc_lst_1[idx] < asc_lst_2[idx]:
                return False
            elif asc_lst_1[idx] > asc_lst_2[idx]:
                return True
            else:
                continue
        return True

t0 = time.time()
for j in range(1, size):
    key = P_lst[j]
    i = j
    while(i > 0 and larger(P_lst[i-1], key)):
        P_lst[i] = P_lst[i-1]
        i = i-1
    P_lst[i] = key
t1 = time.time()

run_time = t1-t0
with open(out_file, 'w') as f:
    for i, x in enumerate(P_lst):
        if i == size-1:
            f.write(x)
        else:
            f.write(x+'\n')
    #f.write("input_size: "+str(size)+'\n')
    #f.write("run_time: "+str(run_time)+'\n')

'''     
lst = [54,26,93,17,77,31,44,55,20]
print(lst)
for j in range(1,len(lst)):
    key = lst[j]
    i=j
    while(i>0 and lst[i-1]>key):
        lst[i] = lst[i-1]
        i = i-1
    lst[i] = key
print(lst)
'''