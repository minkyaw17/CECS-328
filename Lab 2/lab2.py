import random


def square_root_ceiling(k):  # O(log n)
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == k:  # if the middle element squared is equal to k, then mid is the answer
            return mid
        elif mid_squared < k:  # if the middle element squared is less than k, move to the upper part
            low = mid + 1
        else:
            high = mid - 1
            ceil = mid  # moving back to mid because we are returning the ceiling, or else it would be - 1

    return ceil


def user_input_sqrt():
    user_input = int(input("Please enter a positive number: "))
    return square_root_ceiling(user_input)


print("Square root (ceiling) of your input:", user_input_sqrt())


def smallest_missing_integer(n, s, e):  # inputting array, start, and end -> O(log n)
    mid = (s + e) // 2

    if s > e:
        return e + 1
    elif n[mid] == mid:  # since there's no missing integer on the left, move to the right
        return smallest_missing_integer(n, mid + 1, e)
    else:  # missing integer on the left, so start from the beginning
        return smallest_missing_integer(n, s, mid - 1)


def test_cases_smi():  # test cases for examples provided in the lab
    a1 = [0, 1, 3, 6, 8, 9]
    len_a1 = len(a1)

    a2 = [2, 5, 7, 11]
    len_a2 = len(a2)

    a3 = [0, 1, 2, 3, 4]
    len_a3 = len(a3)

    a4 = [12]
    len_a4 = len(a4)

    print("\nFirst test case - smallest missing integer:", smallest_missing_integer(a1, 0, len_a1 - 1))
    print("Second test case - smallest missing integer:", smallest_missing_integer(a2, 0, len_a2 - 1))
    print("Third test case - smallest missing integer:", smallest_missing_integer(a3, 0, len_a3 - 1))
    print("Fourth test case - smallest missing integer:", smallest_missing_integer(a4, 0, len_a4 - 1))


test_cases_smi()


def user_input_smi():
    m = int(input("\nEnter a positive integer: "))

    x = list({random.randint(0, m - 1) for i in range(m // 2)})  # Q: wouldn't it be 0 to m - 1?
    len_x = len(x)
    x.sort()

    print(x)

    print("User input test case:", smallest_missing_integer(x, 0, len_x - 1))


user_input_smi()


def ui_smi_two():
    x = list({random.randint(0, 20) for i in range(20 // 2)})
    len_x = len(x)
    x.sort()

    print("\nGenerated array:", x)

    m = int(input("Enter a positive integer greater than the max value of the list: "))

    print("User input test case:", smallest_missing_integer(x, 0, len_x - 1))


ui_smi_two()
