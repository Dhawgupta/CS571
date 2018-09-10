def find_max(l):
    min_ = 0
    max_ = len(l) - 1
    mid = (max_ + min_)/2
    # flag = True
    while True:
        if mid == 0:
            if l[mid] > l[mid+ 1]
                return mid
        if mid == len(l) - 1:
            if l[mid] > l[mid-1]:
                return mid
        if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
            # max element found
            return mid
        else:
            if l[mid - 1] < l[mid + 1]:
                min_ = mid - 1
            else
               max_ = mid + 1
        mid = (min_ + max_)/2
