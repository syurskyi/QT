def index_gen(i, j):
    # index are order as a clock, we start in 'top left' end finish in 'middle left':
    index = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1],
             [i, j - 1]]
    for i, j in index:
        yield i, j


j = [1, 2]
print(type(j))
all_index = [[x, y] for x in range(0, 6) for y in range(0, 6)]
print(all_index)
for x, y in index_gen(j[0], j[1]):
    print(x, y)
    all_index.remove([x, y])

print(all_index)