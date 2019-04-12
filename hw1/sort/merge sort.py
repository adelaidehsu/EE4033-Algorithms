from tools import Parser
import sys
import time

in_file = sys.argv[1]
out_file = sys.argv[2]
myParser = Parser(in_file)
P_lst = myParser.queryList()
size = len(P_lst)

def larger(str1, str2):
    if str2 == float("inf") and not str1 == float("inf"):
        return False
    if str1 == float("inf"):
        return True
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

def Merge(P_lst, head, m1, m2, tail):
    l_lst = P_lst[head:m1]
    m_lst = P_lst[m1:m2]
    r_lst = P_lst[m2:tail]
    l = 0
    m = 0
    r = 0
    l_lst.append(float("inf"))
    m_lst.append(float("inf"))
    r_lst.append(float("inf"))
    for i in range(head,tail):
        if larger(m_lst[m], l_lst[l]) and larger(r_lst[r], l_lst[l]):
            P_lst[i] = l_lst[l]
            l+=1
        elif larger(l_lst[l], m_lst[m]) and larger(r_lst[r], m_lst[m]):
            P_lst[i] = m_lst[m]
            m+=1
        elif larger(l_lst[l], r_lst[r]) and larger(m_lst[m], r_lst[r]):
            P_lst[i] = r_lst[r]
            r+=1
'''
        if l_lst[l] <= m_lst[m] and l_lst[l] <= r_lst[r]:
            P_lst[i] = l_lst[l]
            l+=1
        elif m_lst[m] <= l_lst[l] and m_lst[m] <= r_lst[r]:
            P_lst[i] = m_lst[m]
            m+=1
        elif r_lst[r] <= l_lst[l] and r_lst[r] <= m_lst[m]:
            P_lst[i] = r_lst[r]
            r+=1
'''

def MergeSort(P_lst, head, tail):
    if((tail-head) < 2):
        return
    m1 = head+ int((tail-head)/3)
    if((tail-head)%3!=0):
        m1+=1
    m2 = m1 + int((tail-head)/3)
    if((tail-head)%3==2):
        m2+=1
    MergeSort(P_lst, head, m1)
    MergeSort(P_lst, m1, m2)
    MergeSort(P_lst, m2, tail)
    Merge(P_lst, head, m1, m2, tail)


t0 = time.time()
MergeSort(P_lst, 0, size)
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
lst = [1000, 999, 43, 22, 1, 0]
print(lst)
MergeSort(lst, 0, len(lst))
print(lst)
'''