k: int = 1
answer = 100
myx = 0
for x in range(10000):
    x = x / 1000
    y = (k ** 2 + (x * k) ** 2) ** 0.5 / (k ** 2 + (k + x * k) ** 2) ** 0.5
    if y < answer:
        answer = y
        myx = x
print(answer, myx)
