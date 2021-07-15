def combine(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            num1 = str(arr[i]) + str(arr[j])
            num2 = str(arr[j]) + str(arr[i])
            if int(num1) > int(num2):
                pass
            else:
                arr[i], arr[j] = arr[j], arr[i]
    arr = [str(num_) for num_ in arr]
    return int("".join(arr))


if __name__ == "__main__":
    num = [44, 50, 6, 5, 9]

    print(combine(num))
