from counter import Counter

c1 = Counter()
c2 = Counter()
c3 = Counter(10)

c1.increment()
c1.increment()

c2.increment()

c3.decrement()
c1.reset()

print(c1.count)
print(c2.count)
print(c3.count)
