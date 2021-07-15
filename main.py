def condition(key: int, num_: int):

    str_num1 = str(key)
    str_num2 = str(num_)

    if int(str_num1[0]) > int(str_num2[0]):
        result = True
    elif int(str_num1[0]) == int(str_num2[0]) and len(str_num1) < len(str_num2):
        result = True
    else:
        result = False

    return result


def compare(n, m):
    if int(n[0]) > int(m[0]):
        return True
    elif int(n[0]) == int(m[0]) and len(n) <= len(m):
        if len(n) > 1:
            compare(n[1:], m[1:])
        else:
            return True
    else:
        return False


def large_number(arr: list) -> int:
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and compare(str(key), str(arr[j])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    str_arr = [str(num_) for num_ in arr]

    return int("".join(str_arr))


if __name__ == "__main__":
    num = [44, 50, 6, 5, 9]

    print(large_number(num))
