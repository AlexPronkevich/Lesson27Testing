from counter import Counter

c1 = Counter()
c2 = Counter()
c3 = Counter(10)

c1.increment()
c1.increment()

c2.increment()

c3.decrement()
c1.reset()

# c1.set_count(10)
# n = c1.get_count()
# c1.del_count()

c1.count = 10
n = c1.count
c1.count

print(c1.count)
print(c2.count)
print(c3.count)
