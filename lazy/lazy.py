from timeit import Timer

def generator(file_name):
    for row in open(file_name, "r"):
        yield row

def reader(file_name):
    file = open(file_name, "r")
    result = file.read().split("\n")
    return result

def tester(func):
    csv_data = func("beeg-data.csv")
    row_count = 0
    for row in csv_data:
        row_count += 1

    return row_count

def main():
    z = Timer("tester(generator)", "from __main__ import tester, generator")
    print("Using generator: %f seconds" % z.timeit(number=5))

    y = Timer("tester(reader)", "from __main__ import tester, reader")
    print("Using reader: %f seconds" % y.timeit(number=5))

main()

