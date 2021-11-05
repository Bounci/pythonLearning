# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/24
# description：(2路)归并排序 ①递归式

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


def merge_sort_recursion(lists, left, right):
    """
    递归地实现归并排序。

    :param lists: 待排序列表
    :param left: 子列表索引起始
    :param right: 子列表索引结束
    :return: 对序列进行归并排序结果
    """
    # 子序列中元素少于两个，则退出递归
    if right < left + 1:
        return lists
    mid = (left + right) // 2  # 划分子序列
    merge_sort_recursion(lists, left, mid)
    merge_sort_recursion(lists, mid + 1, right)
    merge(lists, left, mid, right)  # 治：合并两子序列


def merge_sort(lists):
    """
    归并排序
    """
    list2sort = lists.copy()  # 复制待排序列表
    merge_sort_recursion(list2sort, 0, len(list2sort) - 1)
    return list2sort


if __name__ == '__main__':
    lists1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print("原数据：", lists1)
    print("（2路）归并排序(递归)结果：", merge_sort(lists1))
