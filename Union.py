a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = []

# add elements of a
for x in a:
    if x not in union:
        union.append(x)

# add elements of b
for x in b:
    if x not in union:
        union.append(x)

union.sort()
print(union)