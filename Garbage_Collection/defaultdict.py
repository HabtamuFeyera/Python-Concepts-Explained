from collections import defaultdict

# initialize with a default integer value, i.e 0
d = defaultdict(int)
d['one'] = 1
d['two'] = 2
print(d.items())
print(d['green'])

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])