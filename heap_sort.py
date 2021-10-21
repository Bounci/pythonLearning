# author：57213
# time：2021/10/9
# description：堆排序，索引从0开始计算

def swap(arr, a, b):
    """
    交换数组中两个元素位置。
    """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def build_heap(arr, n):
    """
    将欲排序数组构建为大根堆。

    :return: 构建好的大根堆
    """
    '''
    n：数组长度
    '''
    # 利用索引“自下而上”构建大根堆
    for i in range((n // 2 - 1), -1, -1):
        heapfier(arr, n, i)


def heapfier(arr, n, parent):
    """
    堆构建器。

    :return: 调整好的堆。
    """
    '''
    parent：堆的根节点索引号
    n：数组长度
    '''
    # 基本要求子节点索引小于数组长度
    if 2 * parent + 2 < n:
        larger = parent  # 记录当前较大数的索引号
        # 只有左子树的情况（仅在最后一个父节点处考虑）
        if 2 * parent + 1 == n:
            left = 2 * parent + 1
            if arr[parent] < arr[left]:
                larger = left
        # 同时拥有左子树和右子树
        else:
            left = 2 * parent + 1
            right = 2 * parent + 2
            if arr[left] > arr[right] and arr[left] > arr[parent]:
                larger = left
            # 当两个子节点值相等时，若大于父节点，选择替换：右边
            if arr[left] <= arr[right] and arr[right] > arr[parent]:
                larger = right
        if larger != parent:
            swap(arr, parent, larger)
            heapfier(arr, n, larger)


def heap_sort(arr):
    """
    堆排序（大根堆）：①构建大根堆 ②排序、调整大根堆.
    :return: 排序后的数组
    """
    n = len(arr)  # 记录数组长度
    arr1 = arr.copy()  # 防止传入列表被更改
    # 建立大根堆
    build_heap(arr1, n)
    print("初次构建的大根堆：\n", arr1)

    # 排序、调整大根堆（“自上而下”），至堆中还剩2个元素时停止
    for i in range(n - 1, 1, -1):
        swap(arr1, 0, i)  # 交换堆顶至末尾
        n = n - 1  # 数组长度减少1
        heapfier(arr1, n, 0)  # 调整堆，使之保持为大根堆
    return arr1


if __name__ == '__main__':
    # 待排序数列
    # array1 = [1, 4, 6, 8, 3, 7, 9, 10, 2, 5, 6]
    array1 = [75, 87, 68, 92, 88, 61, 77, 96, 80, 72]
    print(array1)
    # 输出堆排序结果
    print(heap_sort(array1))
