import sys

in_file, o_file = sys.argv[1], sys.argv[2]
hw = []
hw_due, hw_p = {}, {}
with open(in_file, 'r') as f:
    for line in f:
        if len(hw)==0: 
            hw = [int(x) for x in line.strip().split(' ')]
        elif len(hw_due)==0:
            for i, d in enumerate(line.strip().split(' ')):
                hw_due[i+1] = int(d)
        elif len(hw_p)==0:
            for i, p in enumerate(line.strip().split(' ')):
                hw_p[i+1] = int(p)

dues = set([d for _ , d in hw_due.items()])
day_hw = {}
for d in dues:
    lst = []
    MAX = -1
    MAX_x = -1
    for x in hw:
        if hw_due[x] == d:
            lst.append(x)
    for x in lst:
        if hw_p[x] > MAX:
            MAX = hw_p[x]
            MAX_x = x
    day_hw[d] = MAX_x

chosen_x = [x for _ , x in day_hw.items()]
unchosen_x = [x for x in hw if x not in chosen_x]
days = hw

for x in unchosen_x:
    MIN = float("inf")
    MIN_x = -1
    MIN_d = -1
    found = False
    x_d = hw_due[x]
    for d in days:
        if d in day_hw:
            if (d <= x_d) and (hw_p[day_hw[d]] < hw_p[x]) and (hw_p[day_hw[d]] < MIN):
                MIN = hw_p[day_hw[d]]
                MIN_x = day_hw[d]
                MIN_d = d
        elif d <= x_d:
            day_hw[d] = x
            found = True
            break
    if (not found) and MIN_d != -1:
        day_hw[MIN_d] = x

chosen_x = [x for _ , x in day_hw.items()]
unchosen_x = [x for x in hw if x not in chosen_x]
i = 0
for d in days:
    if d not in day_hw:
        day_hw[d] = unchosen_x[i]
        i+=1
sort_day_hw = sorted(day_hw.items())

with open(o_file, 'w')as o:
    idx = 0
    t_p = 0
    for _, x in sort_day_hw:
        if idx == len(sort_day_hw)-1:
            o.write(str(x)+'\n')
        else:
            o.write(str(x)+' ')
        idx+=1
    for x in unchosen_x:
        t_p+=hw_p[x]
    o.write(str(t_p))

