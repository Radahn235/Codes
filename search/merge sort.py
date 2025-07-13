def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # manually append remaining items
    for k in range(i, len(left)):
        res.append(left[k])
    for k in range(j, len(right)):
        res.append(right[k])
    return res

arr = [8, 3, 1, 7, 0, 10, 2]
ori = mergesort(arr)
print("sorted:", ori)
 