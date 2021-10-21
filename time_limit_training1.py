"""
@author：Deng
@time：2021/10/20
@function：三个简单排序练习（升序）
"""


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def bubble_sort(arr):
    """
    冒泡排序：依次比较相邻两元素，将小的换至前面
    """
    arr2sort = arr.copy()
    n = len(arr)  # 数组长度
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arr2sort[j] > arr2sort[j + 1]:
                swap(arr2sort, j, j + 1)
    return arr2sort


def selection_sort(arr):
    """
    选择排序：将数组中较小的数筛选出来放置前面。
    """
    arr2sort = arr.copy()
    n = len(arr)  # 数组长度

    for i in range(0, n - 1):
        min_index = i  # 记录当前最小数的索引
        for j in range(i + 1, n):
            if arr2sort[min_index] > arr2sort[j]:
                min_index = j
        swap(arr2sort, i, min_index)
    return arr2sort


def insert_sort(arr):
    """
    插入排序：将无序部分的元素依次插入有序区域中。
    ！！！第i个元素在交换元素顺序时会发生变化，所以要用一个变量记录原始数据
    """
    arr2sort = arr.copy()
    n = len(arr)  # 数组长度
    for i in range(1, n):
        current = arr2sort[i]
        for j in range(i - 1, -1, -1):  # range的上下限设定要小心！！！要取到0上限应该为-1，不是1
            if current < arr2sort[j]:
                arr2sort[j + 1] = arr2sort[j]
                continue
            else:
                arr2sort[j + 1] = current
                break

    # for i in range(1, n, 1):
    #     j = i - 1
    #     current = arr2sort[i]
    #     while current < arr2sort[j] and j >= 0:
    #         arr2sort[j + 1] = arr2sort[j]
    #         j = j - 1
    #     arr2sort[j + 1] = current
    return arr2sort


if __name__ == '__main__':
    # 待排序数列
    array1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print(array1)
    # 冒泡排序
    print(bubble_sort(array1))
    # 选择排序
    # print(selection_sort(array1))
    # 插入排序
    print(insert_sort(array1))
