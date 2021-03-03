import random
import time


def swap(arr, a, b):  # swap function to be used in the heap sort and selection sort
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
    # when it gets here, l > r and r crosses l, so we swap the pivot with l
    swap(arr, arr.index(pivot), l)

    return l


def quick_sort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quick_sort(a, left, pivot - 1)
        quick_sort(a, pivot + 1, right)


def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def sorting_program():
    n = int(input("Please enter a positive integer: "))

    a = [random.randint(-5000, 5000) for i in range(n)]

    rd = list(set(a))  # making it a set for efficiency

    a2 = a[:]

    rd2 = list(set(a2))  # making it a set for efficiency

    start_qs = time.time_ns()
    for i in range(100):
        quick_sort(rd, 0, len(rd) - 1)
    stop_qs = time.time_ns()

    end_qs = (stop_qs - start_qs) / 100

    # print(rd)

    print("Average time of quick sort for user input:", end_qs, "ns")

    start_is = time.time_ns()
    for i in range(100):
        insertion_sort(rd2, len(rd2))
    stop_qs = time.time_ns()

    end_is = (stop_qs - start_qs) / 100

    # print(rd2)

    print("Average time of insertion sort for user input:", end_is, "ns")

    # instructions per sec
    instructions = end_is / n ** 2  # O(n^2) for insertion sort
    one_sec = 1e9 / instructions

    print("Instructions for my computer running insertion sort in a second:", one_sec, "instructions")


sorting_program()
