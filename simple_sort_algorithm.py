# author：57213
# time：2021/9/23
# description：排序算法学习


def bubble_sort(arr):
    """
    冒泡排序（升序）：相邻数据两两对比，将小的数排在前.

    :return: 排序后的数组
    """
    n = len(arr)  # 记录数组长度
    arr1 = arr.copy()  # 防止传入列表被更改

    for i in range(0, n - 1, 1):
        # 循环比较当前数与后面乱序区的数，range不包括上界
        for j in range(0, n - i - 1, 1):
            if arr1[j] > arr1[j + 1]:
                temp = arr1[j]
                arr1[j] = arr1[j + 1]
                arr1[j + 1] = temp
    return arr1


def selection_sort(arr):
    """
    选择排序（升序）：逐步寻找最小元素放在数组最前面.

    :return: 排序后的数组
    """
    n = len(arr)  # 记录数组长度
    arr1 = arr.copy()  # 防止传入列表被更改

    for i in range(0, n - 1, 1):
        min_index = i
        # 查找最小元素索引
        for j in range(i + 1, n, 1):
            if arr1[min_index] > arr1[j]:
                min_index = j
        temp = arr1[i]
        arr1[i] = arr1[min_index]
        arr1[min_index] = temp
    return arr1


def insert_sort(arr):
    """
    插入排序（升序）：将未排序数插入至有序区合适的位置.

    :return: 排序后的数组
    """
    n = len(arr)  # 记录数组长度
    arr1 = arr.copy()  # 防止传入列表被更改
    # 遍历无序数
    for i in range(1, n, 1):
        preindex = i - 1  # 当前数前面有序区最大索引
        current = arr1[i]  # 保存新一轮要排序的数
        # 将当前数插入有序区合适位置(倒着比较，挨得最近的数为有序区最大数)，将其前面值大于它的数后移
        while current < arr1[preindex] and preindex >= 0:  # 逻辑运算使用and/or/not
            arr1[preindex + 1] = arr1[preindex]
            preindex = preindex - 1  # 无自减运算
        arr1[preindex + 1] = current
    return arr1


if __name__ == '__main__':
    # 待排序数列
    array1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print(array1)
    # 冒泡排序
    # print(bubble_sort(array1))
    # 选择排序
    # print(selection_sort(array1))
    # 插入排序
    print(insert_sort(array1))
