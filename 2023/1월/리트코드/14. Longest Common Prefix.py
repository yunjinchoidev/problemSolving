def binary_search(target):
    s = 0
    e = target

    while s <= e:
        mid = (s+e)//2
        if mid*mid == target:
            return True
        elif mid*mid < target:
            s = mid+1
        else:
            e = mid -1
    return False

binary_search(16)