
def isMaxHeap(arr, n):  # parameter of n for length of array

    for i in range(n // 2):  # going from the root until the last internal node -> O(n)
        left_child = (2 * i) + 1  # left child index
        right_child = (2 * i) + 2  # right child index

        if left_child < n and arr[left_child] > arr[i]:  # if a left child exists and it's bigger than the current
            # internal node
            return False
        if right_child < n and arr[right_child] > arr[i]:  # if a right child exists and it's bigger than the current
            # internal node
            return False
    return True


def check_max_heap():
    arr = [6, 0, 2, 4, 6, 1, 0]
    # arr = [10, 8, 7, 5, 2, 1]
    n = len(arr)

    if isMaxHeap(arr, n):
        print("This is a max-heap.")
    else:
        print("This is NOT a max-heap.")


# check_max_heap()

def binary_search(arr, s, e, key):  # Since we're doing a binary seacrch in a sorted array, the time complexity is O(log n)
    # space complexity is also O(log n) since it's recursive
    mid = (s + e) // 2
    if s <= e:
        if arr[mid] > key:  # if the middle is greater than key, search the lower side
            return binary_search(arr, s, mid - 1, key)
        elif arr[mid] < key:  # if the middle is less than key, search the upper side
            return binary_search(arr, mid + 1, e, key)
        else:
            return mid   # if mid is key, then return index of key
    return -1  # can't return False because we are using index


def isSubSet(original, subset):
    len_original = len(original)
    len_subset = len(subset)

    for i in range(len_subset):
        if binary_search(original, 0, len_original - 1, subset[i]) == -1:
            return False
    return True


def check_subset():
    original = [0, 2, 4, 8, 9, 12, 13, 15, 24]
    subset = [6, 0, 4, 19, 35]

    if isSubSet(original, subset):
        print("b is a subset of a.")
    else:
        print("b is NOT a subset of a.")

# check_subset()


def isSubset_linear(og, sub):
    len_sub = len(sub)
    for i in range(len_sub):
        if sub[i] in og:
            continue
        else:
            return False
    return True


def check_subset_linear():
    original = [0, 2, 4, 8, 9, 12, 13, 15, 24]
    subset = [6, 0, 4, 19, 35]

    if isSubset_linear(original, subset):
        print("b is a subset of a.")
    else:
        print("b is NOT a subset of a.")


check_subset_linear()
