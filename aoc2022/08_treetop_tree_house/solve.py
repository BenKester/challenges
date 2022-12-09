from operator import add

trees = []
with open('input.txt') as file:
    for row in file:
        trees += [[int(c) for c in row.strip()]]
size = len(trees), len(trees[0])
print(f'imported the {size} grid')
visible_count = 0
for i in range(0, size[0]):
    for j in range(0, size[1]):
        visible = False
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            pos = [i, j]
            current = trees[pos[0]][pos[1]]
            while True:
                pos = list(map(add, pos, direction))
                if min(pos) < 0:
                    visible = True
                    break
                elif sum([1 if a>=b else 0 for a, b in zip(pos, size)]):
                    visible = True
                    break
                next = trees[pos[0]][pos[1]]
                if next >= current:
                    break
        if visible:
            visible_count += 1

print(f'{visible_count} trees visible')
max_scenic_score = 0
scores = [[None]*size[1]]*size[0]
for i in range(0, size[0]):
    for j in range(0, size[1]):
        scenic_score = 1
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            pos = [i, j]
            current = trees[pos[0]][pos[1]]
            score = 0
            while True:
                pos = list(map(add, pos, direction))
                if min(pos) < 0:
                    visible = True
                    break
                elif sum([1 if a>=b else 0 for a, b in zip(pos, size)]):
                    visible = True
                    break
                score += 1
                next = trees[pos[0]][pos[1]]
                if next >= current:
                    break
            scenic_score *= score
        scores[i][j] = scenic_score
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
print(f'max scenic score: {max_scenic_score}')
