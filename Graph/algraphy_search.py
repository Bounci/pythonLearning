# -*- coding: utf-8 -*-
# author：Deng
# description：图的遍历搜索

from Graph import ALGraph

# 遍历标记列表
visited = []


def dfs_traverse(graph, vertex):
    """
    深度优先遍历。

    :param graph: 图
    :param vertex: 遍历起始顶点编号。
    """
    # 初始化遍历标记列表
    for i in range(graph.get_vertex_num()):
        visited.append(False)
    al_dfst(graph, vertex)      # 从指定顶点开始深度优先遍历
    # 若由指定顶点开始无法完成图的遍历时，寻找还未遍历过的点，并从其开始进行深度优先遍历
    for i in range(graph.get_vertex_num()):
        if not visited[i]:
            al_dfst(graph, i)
    visited.clear()     # 清空遍历标记列表


def al_dfst(graph, vertex):
    """
    深度优先查找（邻接列表，递归实现）

    :param graph: 图
    :param vertex: 查找起始顶点编号
    """
    index = graph.get_vertex_index_in_list(vertex)  # 获取顶点在头节点表中的【索引值】
    if not visited[index]:
        visited[index] = True
        # 打印当前遍历点【编号】
        print(graph.adjacency_list[index].index)
        # 依次对当前遍历顶点递归地调用深度优先查找
        head_node = graph.adjacency_list[index]
        node = head_node.first_arc
        while node is not None:
            al_dfst(graph, node.index)
            node = node.next_arc


def bfs_traverse(graph: ALGraph, vertex):
    """
    从指定顶点开始，进行广度优先遍历。

    :param graph: 图
    :param vertex: 遍历起始顶点编号。
    """
    # 初始化遍历标记列表
    for i in range(graph.get_vertex_num()):
        visited.append(False)
    al_bfst(graph, vertex)  # 从指定顶点开始广度优先遍历
    # 当由指定顶点开始无法完成图的遍历时，寻找还未遍历过的点，并从其开始进行广度优先遍历
    for i in range(graph.get_vertex_num()):
        if not visited[i]:
            al_bfst(graph, i)
    visited.clear()  # 清空遍历标记列表


def al_bfst(graph, vertex):
    """
    广度优先查找（邻接列表）。

    :param graph: 图
    :param vertex: 查找起始顶点编号。
    :return:
    """
    index = graph.get_vertex_index_in_list(vertex)  # 获取顶点在头节点表中的【索引值】
    temp_queue = [index]  # 等待遍历的顶点【索引值】队列

    while len(temp_queue) != 0:
        node_index = temp_queue.pop(0)  # 取出队列第一个顶点【索引值】
        # 若当前顶点已遍历过，则跳过（一般是有环存在时，同一顶点会出现多次）
        if visited[node_index]:
            continue
        visited[node_index] = True  # 更新当前顶点的遍历状态
        # 打印当前遍历点【编号】
        print(graph.adjacency_list[node_index].index)
        head_node = graph.adjacency_list[node_index]
        node = head_node.first_arc
        while node is not None:
            index = graph.get_vertex_index_in_list(node.index)  # 获取顶点在头节点表中的【索引值】
            if not visited[index]:
                temp_queue.append(index)
            node = node.next_arc


if __name__ == '__main__':
    # region
    # 用于构造无向图：图由一部分组成
    test_matrix1 = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # 构造无向图
    algraph1 = ALGraph.ALGraph(test_matrix1)
    # 广度遍历测试
    print("①邻接列表图从0开始的广度优先遍历顺序：")
    bfs_traverse(algraph1, 0)
    print("①邻接列表图从1开始的广度优先遍历顺序：")
    bfs_traverse(algraph1, 1)
    # 深度遍历测试
    print("①邻接列表图从0开始的深度优先遍历顺序：")
    dfs_traverse(algraph1, 0)
    print("①邻接列表图从1开始的深度优先遍历顺序：")
    dfs_traverse(algraph1, 1)
    # endregion

    # 用于构造无向图：图由两部分组成
    test_matrix2 = [
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # 0
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 1
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 2
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # 9
    ]
    # 构造无向图
    algraph2 = ALGraph.ALGraph(test_matrix2)
    # 广度遍历测试
    print("②邻接列表图从0开始的广度优先遍历顺序：")
    bfs_traverse(algraph2, 0)
    print("②邻接列表图从1开始的广度优先遍历顺序：")
    bfs_traverse(algraph2, 1)
    # 深度遍历测试
    print("②邻接列表图从0开始的深度优先遍历顺序：")
    dfs_traverse(algraph2, 0)
    print("②邻接列表图从1开始的深度优先遍历顺序：")
    dfs_traverse(algraph2, 1)
