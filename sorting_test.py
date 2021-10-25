# -*- coding: utf-8 -*-
# author：57213
# time：2021/10/24
# description：排序算法测试
import numpy as np
import heap_sort
import simple_sort_algorithm
import merge_sort_iteration
import merge_sort_recursion
import quick_sort
import shell_sort

if __name__ == '__main__':
    size = int(input("请输入欲排序列表（列表数据范围0~1000）长度："))
    lists1 = np.random.randint(0, 1000, size)
    print("       原数据：", lists1)
    print("       插入排序结果：", simple_sort_algorithm.insert_sort(lists1))
    print("       选择排序结果：", simple_sort_algorithm.selection_sort(lists1))
    print("       冒泡排序结果：", simple_sort_algorithm.bubble_sort(lists1))
    print("         堆排序结果：", heap_sort.heap_sort(lists1))
    print("       快速排序结果：", quick_sort.quick_sort(lists1))
    print("二路归并：")
    print("归并排序（迭代）结果：", merge_sort_iteration.merge_sort(lists1))
    print("归并排序（递归）结果：", merge_sort_recursion.merge_sort(lists1))
    print("       希尔排序结果：", shell_sort.shell_sort(lists1))