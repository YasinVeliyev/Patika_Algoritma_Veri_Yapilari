# arr = [16, 21, 11, 8, 12, 22]

def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    center = len(arr) // 2
    left = merge_sort(arr[:center])
    right = merge_sort(arr[center:])
    print(left, right)
    new_arr: list = []
    while right and left:
        for i in range(len(left)):
            if left[0] < right[0]:
                new_arr.append(left.pop(0))
                break
            else:
                new_arr.append(right.pop(0))
                break

    else:
        new_arr += left + right

    return new_arr


print(merge_sort([16, 21, 11, 8, 12, 22]))
