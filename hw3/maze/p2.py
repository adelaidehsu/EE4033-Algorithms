import sys

class Stack():

    def __init__(self):
        self.stk = []

    def pop(self):
        """raises IndexError if you pop when it's empty"""
        return self.stk.pop()

    def push(self, elt):
        self.stk.append(elt)

    def is_empty(self):
        return len(self.stk) == 0

    def peek(self):
        if not self.stk.is_empty():
            return self.stk[-1]


class Queue():

    def __init__(self):
        self.q = Stack()  # the primary queue
        self.b = Stack()  # the reverse, opposite q (a joke: q vs b)
        self.front = None

    def is_empty(self):
        return self.q.is_empty()

    def peek(self):
        if self.q.is_empty():
            return None
        else:
            return self.front

    def enqueue(self, elt):
        self.front = elt
        self.q.push(elt)

    def dequeue(self):
        """raises IndexError if you dequeue from an empty queue"""
        while not self.q.is_empty() > 0:
            elt = self.q.pop()
            self.b.push(elt)
        val = self.b.pop()
        elt = None
        while not self.b.is_empty() > 0:
            elt = self.b.pop()
            self.q.push(elt)
        self.front = elt
        return val


def isValid(row, col, total_row, total_col):
    return (row >= 0) and (row < num_row) and (col >= 0) and (col < num_col)

def BFS(maze, src, dst, visited, dr, dc, num_row, num_col, pi):
    visited[src[0]][src[1]] = True
    pi[src[0]][src[1]] = 0

    q = Queue()  
    q.enqueue((src, 0))
    while(not q.is_empty()):
        curr = q.dequeue()
        print(curr)
        pt = curr[0]
        if (pt==dst): 
            return (curr, pi)
        
        for i in range(4):
            row = pt[0] + dr[i]
            col = pt[1] + dc[i]
            if(isValid(row, col, num_row, num_col) and not visited[row][col] and maze[row][col]!='0'):
                visited[row][col] = True
                q.enqueue(((row, col), curr[1]+1))
                pi[row][col] = curr[0]
    return -1

def trace(pi, pt):
    route = []
    while(pi[pt[0]][pt[1]] != 0):
        prev = pi[pt[0]][pt[1]]
        if (prev[0] < pt[0] and prev[1] == pt[1]):
            route.append('3')
        elif(prev[0] > pt[0] and prev[1] == pt[1]):
            route.append('1')
        elif(prev[0] == pt[0] and prev[1] < pt[1]):
            route.append('2')
        elif(prev[0] == pt[0] and prev[1] > pt[1]):
            route.append('4')
        pt = prev
    return route

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    maze, visited, pi = [], [], []
    src, dst = -1, -1
    row_cnt = 0

    with open(in_file ,'r') as f:
        for line in f:
            row = line.strip().split()
            if '2' in row:
                src = (row_cnt, row.index('2'))
            if '3' in row:
                dst = (row_cnt, row.index('3'))
            v_row = [False for _ in range(len(row))]
            pi_row = [-1 for _ in range(len(row))]
            maze.append(row)
            visited.append(v_row)
            pi.append(pi_row)
            row_cnt+=1

    num_row = len(maze)
    num_col = len(maze[0])
    dr = [-1, 0, 0, 1] 
    dc = [0, -1, 1, 0] 

    result = BFS(maze, src, dst, visited, dr, dc, num_row, num_col, pi)
    if result!=-1:
        (curr, pi) = result
        rev_route = trace(pi, curr[0])
        route = rev_route[::-1]
   
        with open(out_file, 'w') as f:
            f.write(str(' '.join(route)))
            f.write('\n')
            f.write(str(curr[1]))
    else:
        with open(out_file, 'w') as f:
            f.write(str(-1))