import run_python 
import run_cython
import time

n = 100000

start = time.perf_counter()
run_python.test(n)
end = time.perf_counter()
python_time = end - start

print(f'{python_time: .8f} second(s) for python')

start = time.time()
run_cython.test(n)
end = time.time()
cython_time = end - start

print(f'{cython_time: .8f} second(s) for cython')
