import math

def load_monkey(filename:str='input.txt'):
    with open(filename) as file:
        monkey = {}
        for row in file:
            match row.strip().split(' '):
                case ['Starting', 'items:', *vals]:
                    monkey['items'] = [int(val.replace(',', '')) for val in vals]
                case ['Monkey', num]:
                    monkey['number'] = int(num[0])
                case ['Operation:', 'new', '=', a, op, b]:
                    monkey['operation'] = {'a': a, 'op': op, 'b': b}
                case ['Test:', 'divisible', 'by', val]:
                    monkey['test'] = int(val)
                case ['If', condition, 'throw', 'to', 'monkey', val]:
                    monkey[f'throw_{condition[:-1]}'] = int(val)
                case ['']:
                    yield monkey
                    monkey = {}
                case _:
                    raise ValueError(f'row "{row}" not expected')
    yield monkey

monkeys = [monkey for monkey in load_monkey(filename='input.txt')]

def simulate(monkeys:list, rounds=20, div3=True):
    lcm = math.lcm(*[m['test'] for m in monkeys])
    counter = [[0]]*len(monkeys)
    for round in range(0, rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                op = monkey['operation']
                a, b = [item if x=='old' else int(x) for x in [op['a'], op['b']]]
                new_val = (a+b) if op['op']=='+' else (a*b)
                if div3:
                    new_val = int(new_val / 3)
                new_val = new_val % lcm
                result = str(new_val % monkey['test'] == 0).lower()
                monkeys[monkey[f'throw_{result}']]['items'].append(new_val)
            monkey['inspected'] = monkey.get('inspected', 0) + len(monkey['items'])
            monkey['items'] = []
        print(f'round {round} of {rounds}', end='\r')
    return monkeys

for m in monkeys:
    print(f'{m["number"]}: {m["items"]}')
simulate(monkeys, rounds=10_000, div3=False)
print('after')
for m in monkeys:
    print(f'{m["number"]}: {m["items"]}')
print('monkey business')
print(math.prod([m['inspected'] for m in sorted(monkeys, reverse=True, key=lambda monkey: monkey['inspected'])[0:2]]))
