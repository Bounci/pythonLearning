# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/24
# description：（非正式）桶排序：针对0~1000以内的数


def bucket_sort(lists):
    # 生成桶
    book = [0 for i in range(0, 1000)]
    length = len(lists)  # 待排序列表长度
    # 遍历待排序列表，并在book中记录
    for i in range(0, length):
        book[lists[i]] = book[lists[i]] + 1
    j = 0
    list2sort = []
    # 将book中的数据按升序提取
    while j < len(book):
        if book[j] != 0:
            for k in range(book[j], 0, -1):
                list2sort.append(j)
        j = j + 1
    return list2sort


if __name__ == '__main__':
    # 待排序数列
    lists1 = [75, 87, 68, 92, 88, 61, 77, 96, 80, 72]

    print("原始数据：", lists1)
    print("（简单）桶排序结果：", bucket_sort(lists1))
