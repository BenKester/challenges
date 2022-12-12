from queue import Queue
REVERSE = True

g = {}
with open('input.txt') as file:
    for y, row in enumerate(file):
        if 'E' in row:
            E = f'{row.find("E")},{y}'
        if 'S' in row:
            S = f'{row.find("S")},{y}'
        for x, c in enumerate(row.strip().replace('E', 'z').replace('S', 'a')):
            g[f'{x},{y}'] =ord(c)-ord('a')

Y=y+1
X=len(row.strip())

cost = {cell: 999 for cell in g}

def unvisited_neighbors(pos):
    def check(newx, newy):
        if (0<=newx<X) and (0<=newy<Y) and (cost[f'{newx},{newy}']==999):
            if REVERSE:
                return (g[f'{newx},{newy}']-g[pos])>=-1
            else:
                return (g[f'{newx},{newy}']-g[pos])<=1

    ret = []
    x, y = [int(i) for i in pos.split(',')]
    for s in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
        if check(*s):
            ret.append(f'{s[0]},{s[1]}')
    return ret

q = Queue(maxsize=X*Y)
start = E if REVERSE else S
cost[start] = 0
print(f'+ {start}, cost {cost[start]}')
q.put(start)
while True:
    cur = q.get(block=False)
    print(f'- {cur}, cost {cost[cur]}')
    if (REVERSE and (g[cur] == 0)) or ((not REVERSE) and (cur == E)):
        print(f'{cost[cur]} steps')
        break
    for neighbor in unvisited_neighbors(cur):
        cost[neighbor] = cost[cur] + 1
        print(f'+ {neighbor}, cost {cost[neighbor]}')
        q.put(neighbor)