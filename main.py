def condition(key: int, num_: int):

    str_num1 = str(key)
    str_num2 = str(num_)

    if int(str_num1[0]) >= int(str_num2[0]) and len(str_num1) <= len(str_num2):
        result = True
    else:
        result = False

    return result


def large_number(arr: list) -> int:
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and condition(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    str_arr = [str(num_) for num_ in arr]

    return int("".join(str_arr))


# if __name__ == "__main__":
#     num = [44, 50, 6, 5, 9]
#
#     print(large_number(num))
