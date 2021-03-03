import random
import math


def swap(arr, a, b):  # swap function to be used in the quick sort
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def median(a, b, c):  # getting the median of 3 to set as the pivot
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


def quick_sort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quick_sort(a, low, pivot - 1)
        quick_sort(a, pivot + 1, high)


def mpssM(arr, start, mid, end):
    sL = []
    sR = []

    temp = 0
    for i in range(start, mid + 1):  # populating the left subarray -> O(n)
        temp += arr[i]
        sL.append(temp)

    temp1 = 0
    for i in range(mid + 1, end + 1):  # populating the right subarray -> O(n)
        temp1 += arr[i]
        sR.append(temp1)

    quick_sort(sL, 0, len(sL) - 1)  # sorting the subarrays using heapsort -> O(n log n)
    quick_sort(sR, 0, len(sR) - 1)

    sR.reverse()  # reversing sR -> O(n)
    sMin = math.inf

    i, j = 0, 0
    while (j < len(sR)) and (i < len(sL)):
        s = sL[i] + sR[j]
        if min(s, sL[i], sR[j]) <= 0:
            i += 1
        elif min(s, sL[i], sR[j]) < sMin:
            sMin = min(s, sL[i], sR[j])
            j += 1
        else:
            j += 1

    return sMin


def mpss(arr, start, end):
    if start == end:
        if arr[0] > 0:
            return arr[0]
        else:
            return math.inf

    else:
        mid = (start + end) // 2
        mpssL = mpss(arr, start, mid)  # O(n log n)
        mpssR = mpss(arr, mid + 1, end)  # O(n log n)
        mpssMid = mpssM(arr, start, mid, end)    # O(n log n)
        return min(mpssL, mpssR, mpssMid)


ar = [2, -3, 1, 4, -6, 10, -12, 5.2, 3.6, -8]
x = mpss(ar, 0, len(ar) - 1)
print("Mpss for given example:", round(x, 2))


def mpss_program():
    n = int(input("Enter a positive number of elements to be added to an array: "))
    rand_list = [round(random.uniform(-20, 20), 2) for i in range(n)]
    len_randList = len(rand_list)

    print("Original array:", rand_list)
    mpss_element = mpss(rand_list, 0, len_randList - 1)

    print("Minimum subsequence sum:", round(mpss_element, 2))


mpss_program()

# a = [25,11,20,12,15,5,2,4,1]
# quick_sort(a,0,len(a) - 1)
# print(a)

