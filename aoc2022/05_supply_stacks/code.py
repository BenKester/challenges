from collections import deque
stage = 'stacks'
stacks = [deque() for i in range(0, 9)]
model = 9001

for row in open('input.txt'):
    if stage == 'stacks':
        if '1' in row:
            stage = 'moving'
        else:
            for i in range(0, 9):
                s = row[i*4+1]
                if s != ' ':
                    stacks[i].appendleft(s)

    elif stage == 'moving':
        match row.strip().split(' '):
            case ['']:
                pass
            case ['move', a, 'from', b, 'to', c]:
                a, b, c = int(a), int(b), int(c)
                boxes = [stacks[b-1].pop() for i in range(0, a)]
                if model == 9001:
                    boxes.reverse()
                for b in boxes:
                    stacks[c-1].append(b)
            case _:
                print(row.strip().split(' '))
                print('failed')

for stack in stacks:
    print(stack[-1], end='')