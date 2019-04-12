import sys

def topologicalSort(n, graph): 
    #visited = [False for i in range(n)]
    state = ['white' for i in range(n)]
    stack =[] 
    for i in range(n): 
        #if visited[i] == False: 
        if state[i] == 'white': 
            topologicalSortUtil(i, state, stack, graph) 
    return stack 

def topologicalSortUtil(v, state, stack, graph): 
    #visited[v] = True 
    state[v] = 'grey'
    for i in graph[v]: 
        #if visited[i] == False: 
        if state[i] == 'white':
            topologicalSortUtil(i, state, stack, graph)
        elif state[i] == 'grey':
            raise ValueError('cycle occurs!') 
    state[v] = 'black'
    stack.insert(0, v) 

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
    n, p = -1, -1
    req_sem = []
    edges = []
    with open(in_file, 'r') as f:
        for line in f:
            line = line.strip().split()
            if n==-1 and p==-1:
                n, p = int(line[0]), int(line[1])
            elif len(req_sem)!=n:
                    req_sem.append(int(line[1]))
            else:
                edges.append((int(line[1]), int(line[0])))    #(pre, after)
    #Build Graph
    graph = {}
    for i in range(n):
        row = []
        for pair in edges:
            if pair[0] == i:
                row.append(pair[1])
        graph[i] = row

    #Topo sort
    try:
        order = topologicalSort(n, graph)
    except ValueError:
        with open(out_file, 'w') as f:
            f.write('-1')
    else:
        sem_course = {}
        sem, prev = -1, -1
        for x in order:
            if x==order[0] and (req_sem[x]==0 or req_sem[x]==2):
                sem = 0
                sem_course[sem] = []
                sem_course[sem].append(str(x))
                prev = x
                continue
            elif x==order[0] and req_sem[x]==1:
                sem = 1
                sem_course[sem] = []
                sem_course[sem].append(str(x))
                prev = x
                continue
        
            if x in graph[prev]:
                if req_sem[x] == ((sem+1)%2) or req_sem[x] == 2:
                    sem+=1
                elif req_sem[x] == ((sem+2)%2):
                    sem+=2
                sem_course[sem] = []
                sem_course[sem].append(str(x))

            elif req_sem[x] == sem%2 or req_sem[x]==2:
                sem_course[sem].append(str(x))
            else:
                sem+=1
                sem_course[sem] = []
                sem_course[sem].append(str(x))
            prev = x

        with open(out_file, 'w') as f:
            num_sem = list(sem_course.keys())[-1]+1
            f.write(str(num_sem))
            f.write('\n')
            for i in range(num_sem):
                if i in sem_course and i!=num_sem-1:
                    f.write(' '.join(sem_course[i]))
                    f.write('\n')
                elif i!=num_sem-1:
                    f.write('-1')
                    f.write('\n')
            if num_sem-1 in sem_course:
                f.write(' '.join(sem_course[num_sem-1]))
            else:
                f.write(str(-1))


          


