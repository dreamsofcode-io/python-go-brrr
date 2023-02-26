import random
import copy
from timeit import Timer
from random import randint

nums = random.sample(range(100000), 100000)

def my_own(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)

        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return my_own(low) + same + my_own(high)

def built_in(nums):
    return sorted(nums)

def main():
    y = Timer("built_in(nums)", "from __main__ import built_in, nums")
    print("Using built-in: %f seconds" % y.timeit(number=10))

    z = Timer("my_own(nums)", "from __main__ import my_own, nums")
    print("Using my own: %f seconds" % z.timeit(number=10))


main()
