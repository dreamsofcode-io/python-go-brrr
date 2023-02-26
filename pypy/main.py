import time

start = time.perf_counter()

n = 10000000
total = 0

for i in range(1, n+1):
    total += i**2

end = time.perf_counter()

print(f'{end-start: .8f} second(s)')
