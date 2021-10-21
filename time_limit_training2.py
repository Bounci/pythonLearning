"""
@author：Deng
@time：2021/10/21
@function：简单排序限时练习。
"""


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def insert_sort(arr):
    n = len(arr)
    array2sort = arr.copy()
    for i in range(1, n, 1):
        preindex = i - 1
        current = array2sort[i]
        while current < array2sort[preindex] and preindex >= 0:
            array2sort[preindex + 1] = array2sort[preindex]
            preindex = preindex - 1
        array2sort[preindex + 1] = current
    return array2sort


def bubble_sort(arr):
    n = len(arr)
    array2sort = arr.copy()
    for i in range(n, 1, -1):
        for j in range(1, i):
            if array2sort[j - 1] > array2sort[j]:
                swap(array2sort, j - 1, j)
    return array2sort


def selection_sort(arr):
    n = len(arr)
    array2sort = arr.copy()
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array2sort[min_index] > array2sort[j]:
                min_index = j
        swap(array2sort, min_index, i)
    return array2sort


if __name__ == '__main__':
    # 待排序数列
    array1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print(array1)
    print(bubble_sort(array1))
    print(selection_sort(array1))
    print(insert_sort(array1))
