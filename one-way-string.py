# Function that validate if has until one error comparing two strings
def is_one_away(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 == len_s2:
        error_counter = 0
        for idx, _ in enumerate(s1):
            if s1[idx] != s2[idx]:
                error_counter += 1

        return error_counter <= 1

    i = 0
    count_erors = 0
    while i < len_s2:
        if s1[i + count_erors] == s2[i]:
            i+=1
        else:
            count_erors += 1
            if count_erors > 1:
                return False

    return True

print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
