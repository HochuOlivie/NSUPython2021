n = int(input())
print(
    [
        (x, y, z)
        for x in range(1, n)
        for y in range(1, x + 1)
        for z in range(1, n)
        if x ** 2 + y ** 2 == z ** 2
    ]
)
