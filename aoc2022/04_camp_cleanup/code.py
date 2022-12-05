def process_pairs(scoring, file_name = 'input.txt'):
    for row in open(file_name):
        pair = row.strip().split(',')
        endpoints = [[int(i) for i in p.split('-')] for p in pair]
        yield scoring(endpoints)

def subset_scorer(endpoints):
    if endpoints[0][0] >= endpoints[1][0] and endpoints[0][1] <= endpoints[1][1]:
        return 1
    elif endpoints[0][0] <= endpoints[1][0] and endpoints[0][1] >= endpoints[1][1]:
        return 1
    else:
        return 0

print(sum(s for s in process_pairs(subset_scorer)))

def overlap_scorer(endpoints):
    for a in range(0, 2):
        other = (a + 1) % 2
        for b in range(0, 2):
            if endpoints[other][0] <= endpoints[a][b] <= endpoints[other][1]:
                return 1
    return 0

print(sum(s for s in process_pairs(overlap_scorer)))
