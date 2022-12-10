register = 1
history = [register]

def cycle():
    history.append(register)
    if abs(register - (len(history)-2) % 40) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if (len(history)-1) % 40 == 0:
        print('\n', end='')

cycle()
with open('input.txt') as file:
    for row in file:
        match row.strip().split(' '):
            case ['noop']:
                cycle()
            case ['addx', x]:
                cycle()
                register += int(x)
                cycle()

total = sum([x*i for i, x in enumerate(history) if i % 40 == 20])
print(f'sum: {total}')