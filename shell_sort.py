# -*- coding: utf-8 -*-
# author：Deng
# time：2021/10/22
# function：希尔排序


def shell_sort(lists):
    """
    希尔排序：按照递减的增量将序列分为若干子序列，分别对子序列进行直接插入排序。
    此处按照每次整除2来调整增量。
    """
    list2sort = lists.copy()  # 防止原数据被修改（传递引用）
    length = len(lists)  # 记录列表长度
    gap = length // 2  # 间隔增量
    # 序列增量调整
    while gap > 0:
        # 分别对不同子序列
        for j in range(gap, length):
            current = list2sort[j]
            # 对某一子序列进行插入排序
            while j - gap >= 0 and list2sort[j - gap] > current:
                list2sort[j] = list2sort[j - gap]
                j = j - gap
            list2sort[j] = current
        gap = gap // 2

    return list2sort


if __name__ == '__main__':
    lists1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    print("原数据：", lists1)
    print("希尔排序结果：", shell_sort(lists1))
