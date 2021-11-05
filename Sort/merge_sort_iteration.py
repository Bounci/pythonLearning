# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/23
# description：(2路)归并排序 ②迭代式


def merge(lists, left, mid, right):
    """
    实现将两个有序子表合并为一个有序子表。

    :param lists: 待排序列表
    :param left: 子列表1索引起始
    :param mid: 子列表索引分界
    :param right: 子列表2索引结尾
    :return: 经过一次归并后的列表
    """
    temp = []  # 临时列表
    i = left
    j = mid + 1
    # 比较两子序列元素并排序
    while i <= mid and j <= right:
        if lists[i] <= lists[j]:
            temp.append(lists[i])
            i = i + 1
        else:
            temp.append(lists[j])
            j = j + 1
    # 复制余下未进行比较的元素
    while i <= mid:
        temp.append(lists[i])
        i = i + 1
    while j <= right:
        temp.append(lists[j])
        j = j + 1
    # 将临时表中排好的元素复制回原列表
    for k in range(0, len(temp)):
        lists[left] = temp[k]
        left = left + 1


def merge_sort_iteration(lists, length):
    """
    归并排序的迭代实现。

    :param lists: 待排序列表
    :param length: 子序列长度
    :return: lists
    """
    i = 0
    # 对相邻两子表进行归并
    while i + 2 * length - 1 < len(lists):
        merge(lists, i, i + length - 1, i + 2 * length - 1)
        i = i + 2 * length
    # 某子表长度不为length时
    if i + length - 1 < len(lists):
        merge(lists, i, i + length - 1, len(lists) - 1)


def merge_sort(lists):
    """
    归并排序。
    """
    list2sort = lists.copy()
    length = 1
    # 迭代，不同子序列长度
    while length < len(list2sort):
        merge_sort_iteration(list2sort, length)
        length = 2 * length
    return list2sort


if __name__ == '__main__':
    lists1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print("原数据：", lists1)
    print("（2路）归并排序(迭代)结果：", merge_sort(lists1))
