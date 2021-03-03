import random
import time


def swap(arr, a, b):  # swap function to be used in the heap sort and selection sort
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def max_heapify(arr, i, n):  # parameter n for length of array
    max_element = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    max_element = i

    # if there's a left child of the root and it's greater than the root
    if left < n and arr[left] > arr[max_element]:
        max_element = left

    # if there's a right child of the root and it's greater than the root
    if right < n and arr[right] > arr[max_element]:
        max_element = right

    if max_element != i:
        swap(arr, i, max_element)
        max_heapify(arr, max_element, n)


def build_maxHeap(arr):
    n = len(arr)
    start_range = (n // 2) - 1

    for i in range(start_range, -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr, ind, n):
    build_maxHeap(arr)

    for i in range(n - 1, 0, -1):  # removing the roots one by one until the tree/array becomes empty
        swap(arr, arr.index(arr[i]), arr.index(arr[0]))
        max_heapify(arr, 0, i)


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i  # keeping track of the min index

        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:  # if the element with the min index is greater than the current element,
                # set it equal to that index
                min_index = j

        swap(arr, i, min_index)


def heap_sort_program():
    print("Part A:\n")

    n = int(input("Please enter the number of elements you wish to put into an array (a positive integer): "))
    #  assuming user input will be 1000 and will do 100 reps to check the run time

    a = [random.randint(-100, 100) for i in range(n)]
    a2 = a[:]

    reps = 100

    start_hs = time.time_ns()
    for i in range(reps):
        heap_sort(a, 0, n)
    stop_hs = time.time_ns()

    end_hs = (stop_hs - start_hs) / reps

    print("Average running time for heap sort:", end_hs, "ns")

    start_sc = time.time_ns()
    for i in range(reps):
        selection_sort(a2)
    stop_sc = time.time_ns()

    end_sc = (stop_sc - start_sc) / reps

    print("Average running time for selection sort:", end_sc, "ns")

    time_diff = end_sc - end_hs

    print("Time difference in which heapsort is faster by:", time_diff, "ns")


def manual_heap_sort():
    print("\nPart B:\n")

    size_arr = 10
    a = [random.randint(-100, 100) for i in range(size_arr)]

    print("Original array:", a)

    heap_sort(a, 0, size_arr)

    print("Sorted array:", a)


heap_sort_program()
manual_heap_sort()
