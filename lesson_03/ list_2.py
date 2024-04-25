x = []

if not x:
    result = [[], []]
else:
    p = len(x) // 2
    a = x[:p + len(x) % 2]
    b = x[p + len(x) % 2:]
    result = [a, b]

print(result)