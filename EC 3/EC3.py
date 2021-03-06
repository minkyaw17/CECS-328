import random
import math


def maxSubArray_n(nums):
    max_sum = nums[0]
    current_sum = max_sum
    len_nums = len(nums)

    for i in range(1, len_nums):
        current_sum = max(nums[i] + current_sum, nums[i])
        max_sum = max(current_sum, max_sum)

    return max_sum


def maxCrossingSubarray(arr, low, mid, high):  # very similar to lab 6 but this time, we're setting it to -inf and
    # seeing where the subarray crosses the midpoint
    sml = 0
    left_sum = -math.inf

    for i in range(mid, low - 1, -1):
        sml += arr[i]
        left_sum = max(sml, left_sum)

    smr = 0
    right_sum = -math.inf

    for i in range(mid + 1, high + 1):
        smr = smr + arr[i]
        right_sum = max(smr, right_sum)

    return max(left_sum + right_sum, left_sum, right_sum)


def maxSubArray_dnc(arr, low, high):
    if (low == high):
        return arr[low]
    else:
        mid = (low + high) // 2

        return max(maxSubArray_dnc(arr, low, mid),
                   maxSubArray_dnc(arr, mid + 1, high),
                   maxCrossingSubarray(arr, low, mid, high))


def MSS_program():
    n = int(input("Please enter a positive integer to be the length of the array: "))

    a = [random.randint(-100, 100) for i in range(n)]

    print(a)

    mss_n = maxSubArray_n(a)
    mss_dnc = maxSubArray_dnc(a, 0, n - 1)

    print("MSS with O(n) time complexity:", mss_n)
    print("MSS with O(n log n) time complexity:", mss_dnc)


MSS_program()
