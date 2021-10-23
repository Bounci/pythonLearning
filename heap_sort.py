# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/9
# description：堆排序，索引从0开始计算

def swap(lists, a, b):
    """
    交换列表中两个元素位置。
    """
    temp = lists[a]
    lists[a] = lists[b]
    lists[b] = temp


def build_heap(lists, length):
    """
    将欲排序列表构建为大根堆。

    :return: 构建好的大根堆
    """
    '''
    length：列表长度
    '''
    # 利用索引“自下而上”构建大根堆
    for i in range((length // 2 - 1), -1, -1):
        heapify(lists, length, i)


def heapify(lists, length, parent):
    """
    堆构建器。

    :return: 调整好的堆。
    """
    '''
    parent：堆的根节点索引号
    length：列表长度
    '''
    # 基本要求子节点索引小于列表长度
    if 2 * parent + 2 < length:
        larger = parent  # 记录当前较大数的索引号
        # 只有左子树的情况（仅在最后一个父节点处考虑）
        if 2 * parent + 1 == length:
            left = 2 * parent + 1
            if lists[parent] < lists[left]:
                larger = left
        # 同时拥有左子树和右子树
        else:
            left = 2 * parent + 1
            right = 2 * parent + 2
            if lists[left] > lists[right] and lists[left] > lists[parent]:
                larger = left
            # 当两个子节点值相等时，若大于父节点，选择替换：右边
            if lists[left] <= lists[right] and lists[right] > lists[parent]:
                larger = right
        if larger != parent:
            swap(lists, parent, larger)
            heapify(lists, length, larger)


def heap_sort(lists):
    """
    堆排序（大根堆）：①构建大根堆 ②排序、调整大根堆.
    :return: 排序后的列表
    """
    length = len(lists)  # 记录列表长度
    lists2sort = lists.copy()  # 防止传入列表被更改（传递引用）
    # 建立大根堆
    build_heap(lists2sort, length)
    # print("初次构建的大根堆：\n", lists1)

    # 排序、调整大根堆（“自上而下”），至堆中还剩2个元素时停止
    for i in range(length - 1, 1, -1):
        swap(lists2sort, 0, i)  # 交换堆顶至末尾
        length = length - 1  # 列表长度减少1
        heapify(lists2sort, length, 0)  # 调整堆，使之保持为大根堆
    return lists2sort


if __name__ == '__main__':
    # 待排序数列
    # lists1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    lists1 = [75, 87, 68, 92, 88, 61, 77, 96, 80, 72]
    print("原始数据：", lists1)
    # 输出堆排序结果
    print("堆排序结果：", heap_sort(lists1))
