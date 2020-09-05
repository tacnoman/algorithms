# Check if one array is equals another array, but rotated
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    second_index = None
    for idx, n in enumerate(list2):
        if n == list1[0]:
            second_index = idx
            break
    
    if second_index == None:
        return False

    list_2_len = len(list2)
    for n in list1:
        if n != list2[second_index]:
            return False

        second_index += 1
        if second_index >= list_2_len:
            second_index -= list_2_len
    return True


print(is_rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))
