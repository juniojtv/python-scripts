import time

def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)
g = gera()
# for v in g:
#     print(v)

# for v in range(5):
#     print(next(g))

l1 = [x for x in range(10)]
l2 = (x for x in range(10))
for x in l1:
    print(x)
time.sleep(1)
for x in l2:
    print(x)