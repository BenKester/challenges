def scores(scoring_alg, file_name = 'input.txt'):
    for row in open(file_name):
        yield scoring_alg(row[2], row[0])

def first_score(ours, theirs):
    ours = {'X': 'r', 'Y': 'p', 'Z': 's'}[ours]
    theirs = {'A': 'r', 'B': 'p', 'C': 's'}[theirs]
    base_score = {'r': 1, 'p': 2, 's': 3}[ours]
    if ours == theirs:
        return base_score + 3       # draw
    elif (ours == 'r' and theirs == 's') or (ours == 'p' and theirs == 'r') or (ours == 's' and theirs == 'p'):
        return base_score + 6       # win
    else:
        return base_score + 0       # loss

def second_score(strat, theirs):
    game_score = {'X':0, 'Y':3, 'Z':6}[strat]
    if strat == 'Y':
        ours = {'A':'r', 'B':'p', 'C':'s'}[theirs]
    elif strat == 'X':
        ours = {'A':'s', 'B':'r', 'C':'p'}[theirs]
    elif strat == 'Z':
        ours = {'A':'p', 'B':'s', 'C':'r'}[theirs]
    base_score = {'r': 1, 'p': 2, 's': 3}[ours]
    return game_score + base_score

print('total score')
print(sum([score for score in scores(scoring_alg=first_score)]))

print('second score')
print(sum([score for score in scores(scoring_alg=second_score)]))
