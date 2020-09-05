def most_frequent(given_list):
    table = {}
    max_item = None

    for n in given_list:
        table[n] = table.get(n, 0) + 1
        if max_item == None:
            max_item = n
        elif table[max_item] < table[n]:
            max_item = n

    return max_item


print(most_frequent([1, 3, 1, 3, 2, 1]))
