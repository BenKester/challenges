def calorie_counter(file_name='input.txt'):
    sum = 0
    for row in open(file_name, 'r'):
        if row.strip() == '':
            yield sum
            sum = 0
        else:
            sum += int(row)

max_elf = 0
for elf in calorie_counter():
    if max_elf < elf:
        max_elf = elf

print('largest:')
print(max_elf)

elves = [elf for elf in calorie_counter()]
elves.sort(reverse=True)
print('largest 3:')
print(sum(elves[:3]))