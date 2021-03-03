import random

# Problem 1 method 1
def linear_search(arr, key): # linear search method to find the mode
    count = 0
    len_arr = len(arr)
    for i in range(len_arr):  # Iterates through the whole array, so O(n)
        # Space complexity is also O(n)
        if key == arr[i]:
            count += 1
    return count


# Problem 1 method 2 (binary search)
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


def counter(arr, key):
    len_arr = len(arr)
    index = binary_search(arr, 0, len_arr - 1, key)  # calling the binary search to get the index

    if index == -1:  # if key is not found, return 0
        return 0

    count = 1  # count = 1 because key is already found and we're finding repetitions
    low = index - 1
    while(low >= 0 and arr[low] == key):  # left index has to be at least 0 for if there's at least 1 element
        # checking the left side of the array for repetitions
        count += 1
        low -= 1

    high = index + 1
    while (high < len_arr and arr[high] == key):  # length of the array has to be greater than the index of the right side
        # checking the left side of the array for repetitions
        count += 1
        high += 1

    return count

# Because we call the binary search function, the run time would be O(log n). However, since we also search the left and
# right side after calling the BS function, it would be O(log n) plus the number of times searched for the duplicate.


a = [0, 1, 1, 2, 2, 2, 3, 3, 6]
k = 2
print("Problem 1:")
print(k, "was repeated", counter(a, k), "times")
print()


# Problem 3
def mode():
    n = int(input("Enter the size of an array you want to generate: "))  # size n user input of array
    rand_int = [random.randint(1, n - 1) for i in range(n)]  # O(n) because we're going through the whole array
    # generating a random array based on user input and displaying it
    print(rand_int)

    my_dict = {i: rand_int.count(i) for i in rand_int}  # Time complexity = O(n) because
    # Space complexity = O(1) because it is a HashMap
    # print(my_dict)

    max_dict = max(my_dict.values())  # accessing the max value of the HashMap
    arr = []
    dict_items = my_dict.items()
    # print("Max:", max_dict)

    for k, v in dict_items:  # O(n) - looping through the HashMap to find the max values of the dictionary
        if max_dict == v:  # if the max value in the HashMap is equal to the value iterated here
            arr.append(k)  # append key of the value

        if v > 1:  # if the value is repeated more than once, print the key and the value
            print(k, "was repeated", v, "times")

        # There can be another if statement to check edge case of something like 1 element of each input
        # Ex: [1,2] and 1 and 2 would be repeated 1 time and they would both be the mode
        # I am assuming that the input array would not have such cases

    str_converted = ", ".join(str(i) for i in arr)  # O(n) - converting the list into a string to be displayed

    print("Mode:", str_converted)

#  Since there are 4 for loops, the time complexity would be 4n but with the big O notation, the 4 would be ignored, and
# the time complexity would be O(n)


mode()
