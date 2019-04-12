import sys

def find_Nmin(x):
    collect = []
    Nmin = 0
    if x < 10:
        return 10+x 
    for i in range(9, 1, -1):
        while x%i==0:
            x = x/i
            collect.append(i)
    #descending
    collect.sort(reverse=True)
    for i, num in enumerate(collect):
        Nmin += num*pow(10,i)
    return Nmin

in_file , o_file = sys.argv[1], sys.argv[2]
p_lst = []
Nmin_lst = []
with open(in_file, 'r')as f:
    for line in f:
        p_lst.append(int(line))
with open(o_file, 'w')as o:
    for x in p_lst:
        if x!= p_lst[-1]:
            o.write(str(find_Nmin(x))+'\n')
        else:
            o.write(str(find_Nmin(x)))
