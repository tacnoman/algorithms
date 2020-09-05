# Return the common elements between to arrays

# Solution using hash
def common_elements_hash(list1, list2):
    table = {}

    for value in list1:
        table[value] = True

    numbers = []
    for value in list2:
        if table.get(value):
            numbers.append(value)
    return numbers


# Best solution, using pointers
def common_elements(list_1, list_2):
    index_1 = 0
    index_2 = 0

    list_1.sort()
    list_2.sort()

    len_list_1 = len(list_2)
    len_list_2 = len(list_2)

    repeated_nums = []

    while index_1 < len_list_1 and index_2 < len_list_2:
        if list_1[index_1] == list_2[index_2]:
            repeated_nums.append(list_1[index_1])
            index_1 += 1
            index_2 += 2
            continue

        if list_1[index_1] > list_2[index_2]:
            index_2 += 1
            continue

        index_1 += 1
    
    return repeated_nums


print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))
