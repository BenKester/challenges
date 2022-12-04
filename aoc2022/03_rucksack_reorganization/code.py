def dupes(file_name = 'input.txt'):
    for row in open(file_name):
        yield get_dupe_val(row.strip())

def get_dupe_val(row):
    n = int(len(row)/2)
    first, second = row[:n], row[n:]
    items = {c for c in first}
    for c in second:
        if c in items:
            return get_item_val(c)
    raise ValueError(f'no dupes in {row}')

def get_item_val(c):
    upper_val = (26 if c.isupper() else 0)
    char_val = ord(c.lower()) - ord('a') + 1
    return upper_val + char_val

print(sum(d for d in dupes()))

def badges(file_name = 'input.txt'):
    rows = []
    for row in open(file_name):
        rows.append(set(row.strip()))
        if len(rows) == 3:
            badge = rows[0].intersection(rows[1], rows[2])
            if len(badge) != 1:
                raise ValueError(f'unexpected badge {badge}')
            yield get_item_val(list(badge)[0])
            rows = []


print(sum(badge for badge in badges()))

## ehh. late night, optimizing for dev time.