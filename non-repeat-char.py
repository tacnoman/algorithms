# Implement your function below.
def non_repeating(given_string):
    letters = {}
    for letter in given_string:
        letters[letter] = letters.get(letter, 0) + 1

    for key, value in letters.items():
        if value == 1:
            return key
    return None


# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab"))   # should return 'c'
print(non_repeating("abab"))    # should return None
print(non_repeating("aabbbc"))  # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'
