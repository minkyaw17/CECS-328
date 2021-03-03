def split_array(arr, key):
    low = 0
    high = len(arr) - 1

    index = -1  # setting index at -1 in case there's no 1s

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= key:  # an if else for even if we found the key, you would keep searching to the left
            high = mid - 1
        else:
            low = mid + 1

        if arr[mid] == key:
            index = mid

    return index


def split_array_program():
    a = []

    k = int(input("Please enter the number of 0s you would like in your binary array: "))

    for i in range(k):
        a.append(0)

    ones = int(input("Please enter the number of 1s you would like in your binary array: "))

    for i in range(ones):
        a.append(1)

    print(a)

    position = split_array(a, 1)

    if position == -1:
        print("No 1s in the array")
    else:
        print("First index of 1:", position)


split_array_program()


def median(a1, a2):
    m = len(a1)
    n = len(a2)
    if m > n:  # if the first array size is bigger , swap
        a1 = a2
        a2 = a1
        m = n
        n = m
    low = 0
    high = m
    half_len = (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half_len - i
        if i < m and a2[j - 1] > a1[i]:
            # increase if i is too small
            low = i + 1
        elif i > 0 and a1[i - 1] > a2[j]:
            # decrease if i is too big
            high = i - 1
        else:
            # i = perfect

            if i == 0:
                max_of_left = a2[j - 1]
            elif j == 0:
                max_of_left = a1[i - 1]
            else:
                max_of_left = max(a1[i - 1], a2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = a2[j]
            elif j == n:
                min_of_right = a1[i]
            else:
                min_of_right = min(a1[i], a2[j])

            return (max_of_left + min_of_right) / 2


a1 = [0, 2, 10, 26, 68]
a2 = [1, 11, 18, 20, 41]

print("Median of merged array:", median(a1, a2))

# https://www.youtube.com/watch?v=LPFhl65R7ww
# Youtube video I watched for part 2 of this EC
