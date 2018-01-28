# Basic Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)/2]
    less = []
    eq = []
    more = []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            eq.append(i)
        else:
            more.append(i)
    return quicksort(less) + eq + quicksort(more)

# Mergesort
def merge(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[0] <= b[0]:
        return a[:1] + merge(a[1:], b)
    else:
        return b[:1] + merge(a, b[1:])
    
def mergesort(arr):
    if len(arr) > 1:
        half = len(arr)/2
        a = mergesort(arr[:half])
        b = mergesort(arr[half:])
        return merge(a, b)
    else:
        return arr

