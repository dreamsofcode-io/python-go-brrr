def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print("using for loop")
for i in simple_generator():
    print(i)

gen = simple_generator()

print("using next")
print(next(gen))
print(next(gen))
print(next(gen))

