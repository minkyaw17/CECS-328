import random


def swap(arr, a, b):  # swapping function
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def median(a, b, c):
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.sort()
    return arr[1]  # the middle element after sorting is the median


def partition(arr, left, right):
    mid = (left + right) // 2  # mid index to be used in the median of the three

    pivot = median(arr[left], arr[mid], arr[right])  # setting the median of the three elements as the pivot
    swap(arr, arr.index(pivot), right)  # swap the pivot with the last element similar to quick sort
    l = left  # storing the left and right variables to use when partitioning
    r = right

    while l < r:
        if arr[l] < pivot:
            l += 1  # increment until left is larger than the pivot
        if arr[r] > pivot:
            r -= 1  # decrement until right is smaller than the pivot
        if l < r:  # when it reaches "the end" it's time to swap
            swap(arr, l, r)   # [1,2,3,5,7,5,4]
            r -= 1
    # when it gets here, l > r and r crosses l, so we swap the pivot with l
    swap(arr, arr.index(pivot), l)

    return l


def quick_select(arr, l, r, k):
    pivIndex = partition(arr, l, r)

    if pivIndex == k:  # if the pivot is the k
        return arr[pivIndex]
    elif pivIndex < k:  # right subarray
        return quick_select(arr, pivIndex + 1, r, k)
    else:  # left subarray
        return quick_select(arr, l, pivIndex - 1, k)


def quick_select_program():
    n = int(input("Please enter the number of elements you wish to put into an array: "))

    rand_list = [random.randint(-100, 100) for i in range(n)]
    arr_len = len(rand_list)
    print(rand_list)

    k = int(input("Please enter a number (k) from 1 to " + str(arr_len) + ": "))

    k_element = quick_select(rand_list, 0, arr_len - 1, k - 1)  # k - 1 because of the index

    print(k, "th least element is", k_element)


print("Part A: QuickSelect\n")
quick_select_program()


def quick_select_max(arr, l, r, k):
    len_arr = len(arr)
    ind = len_arr - k - 1  # this index is to get the last elements of the arr - Ex: k = 2 and len(arr) = 5
    # -> 5 - 2 - 1 = 2 (get the last 2 max elements)
    pivIndex = quick_select(arr, l, r, ind)  # using the quick_select as the pivot index to loop from this index
    # to the length of the array

    list1 = []
    for i in range(arr.index(pivIndex), len_arr):
        list1.append(arr[i])

    return list1


def quick_select_max_program():
    n = int(input("Please enter the number of elements you wish to put into an array: "))

    rand_list = [random.randint(-100, 100) for i in range(n)]
    arr_len = len(rand_list)
    print(rand_list)

    k = int(input("Please enter a number (k) from 1 to " + str(arr_len) + ": "))

    k_element = quick_select_max(rand_list, 0, arr_len - 1, k - 1)  # k - 1 because of the index

    print(k, "max elements are", k_element)

# a = [1,2,2,3,6,8,4]
# k = 2
# k_element = quick_select_max(a, 0, len(a) - 1, k - 1)
# print(k_element)


print("\nPart B: QuickSelectMax\n")
quick_select_max_program()

a = [1,2,2,3,6,8,4]
k = 2
k_element = quick_select_max(a, 0, len(a) - 1, k - 1)
print(k_element)

