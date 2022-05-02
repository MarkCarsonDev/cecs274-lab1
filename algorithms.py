"""Implementations of some sorting"""
import random
import ArrayList

def linear_search(a : ArrayList.ArrayList(), x) -> int:
    for i in range(0, len(a)-1):
        if a[i] == x:
            return i
    return -100

def binary_search(a : ArrayList.ArrayList(), x) -> int:
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2

        # if x is greater, the we can ignore the left half
        if x > a[mid]:
            left = mid + 1
        
        # if x is smaller, we ignore the right half
        elif x < a[mid]:
            right = mid - 1
        
        # else x is equal to value at mid, return index
        else:
            return mid
    return -100

# take two arrays and merge them into a single sorted array
def _merge(a0 : ArrayList.ArrayList(), a1 : ArrayList.ArrayList(), a : ArrayList.ArrayList()):
    i0 = 0
    i1 = 0
    k = 0
    
    # copy data from arrays a0 and a1
    while i0 < len(a0) and i1 < len(a1):
        '''
        if the value of the left array is greater than the value of the right array
        then overwrite the orginal array, a, with the left index's value
        '''
        if a0[i0] <= a1[i1]:
            a[k] = a0[i0]
            i0 += 1
        else:
            '''
            if the value of the right array is greater than the value of the left array
            then overwrite the orginal array, a, with the right index's value
            '''
            a[k] = a1[i1]
            i1 += 1
        k += 1
    
    # if there is any data left in the arrays a0 or a1
    while i0 < len(a0):
        a[k] = a0[i0]
        i0 += 1
        k += 1
    
    while i1 < len(a1):
        a[k] = a1[i1]
        i1 += 1
        k += 1


def merge_sort(a : ArrayList.ArrayList()):
    if len(a) > 1:
        # obtain mid point of array
        mid = len(a) // 2
        # get left half of array
        a0 = a[0:mid]
        # get right half of array
        a1 = a[mid:len(a)]
        # sort left half
        merge_sort(a0)
        # sort right half
        merge_sort(a1)
        # merge the two halves
        _merge(a0, a1, a)
    return a


# runs in O(n log(n)) time
def merge_sort2(a : ArrayList.ArrayList()) -> ArrayList.ArrayList():
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = a[0: m - 1]
    a1 = a[m: len(a) - 1]
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)

# Quicksort Algorithm with first element as pivot
def _quick_sort_f(a : ArrayList.ArrayList(), l, r):
    if l < r:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(a, l, r, l)

        # Recursive call on the left of pivot
        _quick_sort_f(a, l, pi - 1)

        # Recursive call on the right of pivot
        _quick_sort_f(a, pi + 1, r)
    return a

# Quicksort Algorithm with random element as pivot
def _quick_sort_r(a : ArrayList.ArrayList(), i, n):
    if i < n:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        rand = random.randint(i, n)
        pi = partition(a, i, n, rand)

        # Recursive call on the left of pivot
        _quick_sort_r(a, i, pi - 1)

        # Recursive call on the right of pivot
        _quick_sort_r(a, pi + 1, n)
    return a

def quick_sort(a : ArrayList.ArrayList(), p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, len(a)-1)
    else:
        _quick_sort_f(a, 0, len(a)-1)
    return a

def partition_last(a : ArrayList.ArrayList(), start, end):
    pivot = a[end]
    i = start - 1
    for j in range(start, end):
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)
    swap(a, end-1, end)
    return end-1

def partition(a : ArrayList.ArrayList(), start, end, pivot_idx):
    # swap last element with pivot_idx to make pivot the rightmost element
    swap(a, end, pivot_idx)

    pivot = a[end]
    i = start - 1
    for j in range(start, end):
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, end)
    return i + 1

def swap(a : ArrayList.ArrayList(), i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp