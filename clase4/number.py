def number_from_file(filename):
    with open(filename) as f:
        return int(f.read())

print(number_from_file('num.txt'))  