# -*- coding: utf-8 -*-
# author：Deng
# description：图的遍历搜索

from Graph import ALGraph


def dfs_traverse(graph, vertex):
    """
    深度优先遍历。

    :param graph: 图
    :param vertex: 遍历起始顶点。
    """
    pass


def bfs_traverse(graph: ALGraph, vertex):
    """
    广度优先遍历。

    :param graph: 图
    :param vertex: 遍历起始顶点。
    """
    visited = []
    # 初始化遍历标记列表
    for i in range(graph.get_vertex_num):
        visited.append(False)
    for i in range(graph.get_vertex_num):
        


if __name__ == '__main__':
    # 用于构造无向图
    test_matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
