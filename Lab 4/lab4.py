import random


def swap(arr, a, b):
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
            swap(arr, l, r)
    # when it gets here, l > r and r crosses l, so we swap the pivot with arr[l]
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


def abs_partition(arr, left, right):
    mid = (left + right) // 2  # mid index to be used in the median of the three

    pivot = abs(median(arr[left], arr[mid], arr[right]))  # setting the median of the three elements as the pivot
    swap(arr, arr.index(pivot), right)  # swap the pivot with the last element similar to quick sort
    l = left  # storing the left and right variables to use when partitioning
    r = right

    while l < r:
        if abs(arr[l]) < abs(pivot):
            l += 1  # increment until left is larger than the pivot
        if abs(arr[r]) > abs(pivot):
            r -= 1  # decrement until right is smaller than the pivot
        if l < r:  # when it reaches "the end" it's time to swap
            swap(arr, l, r)
    # when it gets here, l > r and r crosses l, so we swap the pivot with arr[l]
    swap(arr, arr.index(pivot), l)

    return abs(l)


def quick_select_abs(arr, l, r, k):
    pivIndex = abs_partition(arr, l, r)

    if pivIndex == k:  # if the pivot is the k
        return arr[pivIndex]
    elif pivIndex < k:  # right subarray
        return quick_select(arr, pivIndex + 1, r, k)
    else:  # left subarray
        return quick_select(arr, l, pivIndex - 1, k)


def quick_select_min(arr, l, r, k):  # getting the closest numbers to the median
    pivIndex = quick_select_abs(arr, l, r, k)

    list1 = []
    for i in range(0, arr.index(pivIndex) + 1):
        list1.append(arr[i])

    return list1


def difference(arr, med):
    len_arr = len(arr)

    diff = []
    for i in range(len_arr):
        arr[i] -= med
        diff.append(arr[i])

    return diff


def quick_select_median_program():
    n = int(input("Please enter the number of elements you wish to put into the array: "))

    a = [random.randint(-100, 100) for i in range(n)]

    print("Your array:", a)

    k = int(input("Please enter a number from 1 to " + str(n) + ": "))

    len_arr = len(a)
    pos = len_arr // 2

    median_element = quick_select(a, 0, len_arr - 1, pos)  # calling quick_select to sort the array, with the position
    # being half the length of the array

    print("Median element:", median_element)

    diff = difference(a, median_element)
    len_diff = len(diff)

    closest_to_median = quick_select_min(diff, 0, len_diff - 1, k)  # calling the quic_select_min function, similar to
    # lab 3 part B to get the elements closest to the median

    for i in range(1, k + 1):
        closest_to_median[i] = closest_to_median[i] + median_element

    print("Numbers closest to median:", closest_to_median[1:])


quick_select_median_program()
