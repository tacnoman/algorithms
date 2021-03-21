import random

numbers = []

MIN = 1
MAX = 10

for i in range(10):
    numbers.append([
        random.randint(MIN, MAX),
        random.randint(MIN, MAX),
    ])

print(numbers)

# def main():
#     pass


# main()
