# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/9
# description：快速排序  定义基准为待排序列表第一个元素

def swap(lists, left, right):
    """
    交换列表中两个元素位置。
    """
    temp = lists[left]
    lists[left] = lists[right]
    lists[right] = temp


def chose_pivot(lists, front):
    """
    选择快排基准。

    :return:基准 pivot
    """
    # 选择列表左边第一个为基准
    pivot = lists[front]
    # 随机选择、三分选择…… 待补充
    # 若选择在其他位置，则交换至最左侧
    return pivot


def quick_core(lists, front, back):
    # 必须满足的索引前提
    if back - front >= 1 and back < len(lists) and front >= 0:
        # 列表第一个元素作为排序基准
        pivot = chose_pivot(lists, front)
        # 从右边开始遍历
        right = back  # 右侧起始索引
        left = front  # 左侧起始索引
        flag = 0  # 0指示从右侧遍历，1指示从左侧遍历
        while right > left:
            if flag == 0:
                if lists[right] >= pivot:
                    right = right - 1
                # 右侧数小于等于基准，交替遍历方向为左侧
                else:
                    swap(lists, left, right)
                    left = left + 1
                    flag = 1
                continue
            if flag == 1:
                if lists[left] < pivot:
                    left = left + 1
                # 左侧数大于基准，交替遍历方向为右侧
                else:
                    swap(lists, left, right)
                    right = right - 1
                    flag = 0
        lists[right] = pivot

        quick_core(lists, front, right - 1)
        quick_core(lists, right + 1, back)


def quick_sort(lists):
    """
    快速排序（升序）：选择一个基准，小于基准的置于左侧，大于等于基准的置于右侧.

    :return: 排序后的列表
    """
    '''
    front：排序序列起始索引
    back：排序序列结束索引
    '''
    lists2sort = lists.copy()  # 防止传入列表被更改（传递引用）
    length = len(lists)  # 记录列表长度
    quick_core(lists2sort, 0, length - 1)
    return lists2sort


if __name__ == '__main__':
    lists1 = [75, 87, 68, 92, 88, 61, 77, 96, 80, 72]
    print("原始数据：", lists1)
    # 输出快速排序结果
    print("快速排序结果：", quick_sort(lists1))
