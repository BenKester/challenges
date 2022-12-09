from operator import add, __sub__
from numpy import clip, mean
n_tails = 9
pos = [[0, 0]]*(1+n_tails)
directions = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
visited = set()

def add_position(new_pos):
    visited.add('.'.join([str(int(x)) for x in new_pos]))

def move_head(old_pos, direction):
    return list(map(add, old_pos, direction))

def move_tail(old_pos, head_pos):
    diff = list(map(__sub__, head_pos, old_pos))
    if max(list(map(abs, diff))) <= 1:
        # tail is adjacent to head, does not move
        return old_pos
    elif sum(list(map(abs, diff))) == 2:
        # tail is 2 away in a straight line, take the average
        return list(mean([old_pos, head_pos], axis=0))
    else:
        # tail is a knight move away, move 1 space diagonally
        # part 2 could be a double diagonal away, still move 1 space diagonally
        return list(map(add, old_pos, clip(diff, -1, 1)))

add_position(pos[-1])
with open('input.txt') as file:
    for row in file:
        direction, count = row.strip().split(' ')
        for i in range(0, int(count)):
            pos[0] = move_head(pos[0], directions[direction])
            for j in range(0, n_tails):
                pos[j+1] = move_tail(pos[j+1], pos[j])
            add_position(pos[-1])

print(f'the last tail has visited {len(visited)} positions')