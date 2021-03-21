import time
import random

numbers = []

for i in range(10000000):
    numbers.append([
        random.randint(1, 100),
        random.randint(1, 100),
    ])


def sum_numbers(n1, n2):
    return n1 + n2


def main():
    all_numbers = []
    for number in numbers:
        n = sum_numbers(number[0], number[1])

        found = False
        for current_number in all_numbers:
            if current_number == n:
                found = True
                break

        all_numbers.append(n)

    return (len(all_numbers))


def main_2():
    all_numbers = {}
    for number in numbers:
        n = sum_numbers(number[0], number[1])

        if all_numbers.get(n, False):
            continue

        all_numbers[n] = True

    return (len(all_numbers.keys()))
    


start = time.time()
main()
end = time.time()
print(end - start)


start = time.time()
main_2()
end = time.time()
print(end - start)
