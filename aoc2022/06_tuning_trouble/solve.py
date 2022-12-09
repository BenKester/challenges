def get_signal(file_name='input.txt', signal_length = 4):
    with open(file_name) as file:
        for row in file:
            i = signal_length
            while True:
                if len(set(row[i-signal_length:i])) == signal_length:
                    return i
                i += 1
                if i > len(row):
                    raise ValueError('process failed')

print(get_signal(signal_length=4))
print(get_signal(signal_length=14))
