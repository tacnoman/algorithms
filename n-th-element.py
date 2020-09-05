class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)


# NTH from last linked list in bad way. Using an array and spending too much memory
def nth_from_last_bad_way(head, n):
    current = head
    if not current:
        return None

    nums = [current.value]

    while current.child != None:
        current = current.child
        nums.append(current.value)

    if n > len(nums):
        return None

    return nums[len(nums)-n]


# Another solution spending memory too, but a few better
def nth_from_last_a_few_better(head, n):
    current = head
    if not current:
        return None

    nums = [current.value]

    while current.child != None:
        current = current.child
        nums.insert(0, current.value)

        nums = nums[0:n]

    if n > len(nums):
        return None

    return nums[n - 1]


# Using pointer to avoid create array to save data
def nth_from_last(head, n): # best solution
    pointer1 = head
    pointer2 = head

    counter = 0

    while pointer2 != None:
        counter += 1
        if counter > n:
            pointer1 = pointer1.child
        pointer2 = pointer2.child
    
    if counter < n:
        return None

    return pointer1.value

# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)

print(nth_from_last(head, 5))
# nth_from_last(head, 1) should return 1.
# nth_from_last(head, 5) should return 5.
# nth_from_last(head2, 2) should return 3.
# nth_from_last(head2, 4) should return 1.
# nth_from_last(head2, 5) should return None.
# nth_from_last(None, 1) should return None.
