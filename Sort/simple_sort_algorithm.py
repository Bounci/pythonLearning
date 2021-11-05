# -*- coding: utf-8 -*-
# author：57213
# time：2021/9/23
# description：排序算法学习


def bubble_sort(lists):
    """
    冒泡排序（升序）：相邻数据两两对比，将小的数排在前.

    :return: 排序后的列表
    """
    length = len(lists)  # 记录列表长度
    lists2sort = lists.copy()  # 防止传入列表被更改（传递引用）

    for i in range(0, length - 1, 1):
        # 循环比较当前数与后面乱序区的数，range不包括上界
        for j in range(0, length - i - 1, 1):
            if lists2sort[j] > lists2sort[j + 1]:
                temp = lists2sort[j]
                lists2sort[j] = lists2sort[j + 1]
                lists2sort[j + 1] = temp
    return lists2sort


def selection_sort(lists):
    """
    选择排序（升序）：逐步寻找最小元素放在列表最前面.

    :return: 排序后的列表
    """
    length = len(lists)  # 记录列表长度
    lists2sort = lists.copy()  # 防止传入列表被更改（传递引用）

    for i in range(0, length - 1, 1):
        min_index = i
        # 查找最小元素索引
        for j in range(i + 1, length, 1):
            if lists2sort[min_index] > lists2sort[j]:
                min_index = j
        temp = lists2sort[i]
        lists2sort[i] = lists2sort[min_index]
        lists2sort[min_index] = temp
    return lists2sort


def insert_sort(lists):
    """
    插入排序（升序）：将未排序数插入至有序区合适的位置.

    :return: 排序后的列表
    """
    length = len(lists)  # 记录列表长度
    lists2sort = lists.copy()  # 防止传入列表被更改（传递引用）
    # 遍历无序数
    for i in range(1, length, 1):
        preindex = i - 1  # 当前数前面有序区最大索引
        current = lists2sort[i]  # 保存新一轮要排序的数
        # 将当前数插入有序区合适位置(倒着比较，挨得最近的数为有序区最大数)，将其前面值大于它的数后移
        while current < lists2sort[preindex] and preindex >= 0:  # 逻辑运算使用and/or/not
            lists2sort[preindex + 1] = lists2sort[preindex]
            preindex = preindex - 1  # 无自减运算
        lists2sort[preindex + 1] = current
    return lists2sort


if __name__ == '__main__':
    # 待排序数列
    lists1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print(lists1)
    # 冒泡排序
    # print(bubble_sort(lists1))
    # 选择排序
    # print(selection_sort(lists1))
    # 插入排序
    print(insert_sort(lists1))
