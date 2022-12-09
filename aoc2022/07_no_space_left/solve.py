from dataclasses import dataclass

class Node:
    def __init__(self, parent, name:str, file_size:int=None):
        self.parent = parent
        self.children = {}
        self.name = name
        self.file_size = file_size
        self.is_dir = self.file_size==None
    def get_child(self, name, **kwargs):
        if not name in self.children:
            self.children[name] = Node(self, name, **kwargs)
        return self.children[name]
    def get_size_recursive(self):
        if self.file_size != None:
            return self.file_size
        else:
            return sum([child.get_size_recursive() for child in self.children.values()])
    def get_small_dir_sizes(self, threshold=100000):
        x = self.get_size_recursive()
        x = x if (x<=threshold and self.is_dir) else 0
        return x + sum([child.get_small_dir_sizes() for child in self.children.values()])
    def get_level(self):
        level = 0
        cur = self
        while cur.parent != None:
            level += 1
            cur = cur.parent
        return level

    def __str__(self):
        cur = ' '*self.get_level() + f'{self.name}: {self.get_size_recursive()}\n'
        for child in self.children.values():
            cur += child.__str__()
        return cur

root = Node(parent=None, name='/')
cwd = root

with open('input.txt') as file:
    for line in file:
        match line.strip().split(' '):
            case ['']:
                pass
            case ['$', 'cd', '..']:
                cwd = cwd.parent
            case ['$', 'cd', '/']:
                cwd = root
            case ['$', 'cd', x]:
                cwd = cwd.get_child(x)
            case ['$', 'ls']:
                pass
            case ['dir', x]:
                _ = cwd.get_child(x)
            case [size, x]:
                _ = cwd.get_child(x, file_size=int(size))

print(f'total directory size: {root.get_size_recursive()}')
print(f'small dir sizes: {root.get_small_dir_sizes()}')
#print(root)

total = 70_000_000
required = 30_000_000
current = root.get_size_recursive()
need_to_delete = (required + current) - total
to_search = [root]
best_delete = root.get_size_recursive()
while True:
    cur = to_search[-1]
    to_search = to_search[:-1] + [v for v in cur.children.values() if v.is_dir]
    cur_value = cur.get_size_recursive()
    if cur_value >= need_to_delete and cur_value < best_delete:
        best_delete = cur_value
    if len(to_search) == 0:
        break
print(f'need to delete: {need_to_delete}')
print(f'best: {best_delete}')