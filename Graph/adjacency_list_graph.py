# -*- coding: utf-8 -*-
# author：57213
# description：图存储结构————邻接列表

# 邻接表图结构存储————头结点类
class Vertex(object):
    def __init__(self, index):
        """初始化头结点。"""
        self.index = index  # 初始化头结点编号
        self.first_arc = None  # 初始化头结点的第一个边结点为None，表示头结点与其他结点间无边（弧）


# 邻接表图结构存储————边结点类
class EdgeNode(object):
    def __init__(self, index, weight=1):
        """
        初始化边结点。

        :param index: 边结点编号
        :param weight: 边的权重，默认为1
        """
        self.index = index  # 初始化边结点的结点编号
        self.weight = weight  # 初始化边结点与头结点间边的权重，默认为1
        self.next_arc = None  # 初始化边结点的下一个结点为None


# 图——邻接列表存储结构
class ALGraph(object):
    def __init__(self, matrix, graph_type=0 | 1):
        """
        使用邻接矩阵生成图的邻接表。

        :param matrix: 邻接矩阵
        :param graph_type: 图的类型，1：无向图（默认）；0：有向图
        """
        self.graph_type = graph_type
        self.__vertex_num = len(matrix)  # 记录图中包含的顶点数量
        self.adjacency_list = []  # 图的邻接列表
        # 判断邻接矩阵是否规范构建
        for row in range(self.__vertex_num):
            if len(matrix[row][:]) != self.__vertex_num:
                raise ValueError("邻接矩阵构建有误！")
        # 以邻接列表存储结构创建图
        self.__creat_adjacency_list_graph(matrix)

    def __creat_adjacency_list_graph(self, matrix):
        """
        通过邻接矩阵构建图的邻接列表。

        :param matrix: 邻接矩阵
        """
        # 建立头结点列表
        for i in range(self.__vertex_num):
            self.adjacency_list.append(Vertex(i))
        # 根据邻接矩阵建立邻接列表
        for row in range(self.__vertex_num):
            for column in range(self.__vertex_num):
                # 跳过对邻接矩阵对角线元素的操作
                if row == column:
                    continue
                # 邻接矩阵中不为0和无穷大处，表示二者间有边
                if matrix[row][column] != 0 and matrix[row][column] != float('inf'):
                    # 无向图
                    if self.graph_type == 1:
                        edge_node = EdgeNode(column, matrix[row][column])
                        self.__insert_edge_node(row, edge_node)  # 向某头结点的邻接列表中插入边结点
                        edge_node_inv = EdgeNode(row, matrix[row][column])
                        self.__insert_edge_node(column, edge_node_inv)  # 向某头结点的邻接列表中插入边结点
                    # 有向图
                    if self.graph_type == 0:
                        edge_node = EdgeNode(column, matrix[row][column])
                        self.__insert_edge_node(row, edge_node)  # 向某头结点的邻接列表中插入边结点

    def __insert_edge_node(self, row, edge_node):
        """
        以头插入的方式，向头结点的邻接表中插入边结点。

        :param row: 头结点在结点表中的索引号。
        :param edge_node: 要插入的边结点。
        """
        # 头结点的边结点指示为None，插入第一个边结点
        if self.adjacency_list[row].first_arc is None:
            self.adjacency_list[row].first_arc = edge_node
        else:
            temp = self.adjacency_list[row].first_arc  # 临时记录头结点指向的第一个边结点
            self.adjacency_list[row].first_arc = edge_node
            edge_node.next_arc = temp  # 插入完成后的当前第一边结点指向原首位边结点

    def get_vertex_num(self):
        """获取图节点数。"""
        return self.__vertex_num

    def __vertex_is_exist(self, index):
        """
        判断某一结点是否存在于图中。

        :return: True:已存在；False:不存在
        """
        for i in range(self.__vertex_num):
            if self.adjacency_list[i].index == index:
                return True
        return False

    def __get_vertex_index_in_list(self, vertex_index):
        """获得顶点在头结点列表中的索引值。"""
        for index in range(self.__vertex_num):
            if self.adjacency_list[index].index == vertex_index:
                return index

    def get_edge_value(self, start, end):
        """
        获取边的权值。

        :param start: 对于有向图，边的起点的编号
        :param end: 对于有向图，边的终点的编号
        :return: 边的权重值
        """
        # 寻找边权重的前提：边的两个顶点均存在。
        if self.__vertex_is_exist(start) and self.__vertex_is_exist(end):
            weight = 0
            index = self.__get_vertex_index_in_list(start)
            edge_node = self.adjacency_list[index].first_arc
            while edge_node is not None:
                if edge_node.index == end:
                    weight = edge_node.weight
                edge_node = edge_node.next_arc
            return weight
        else:
            raise ValueError("边不存在！")

    def get_vertex_degree(self, vertex):
        """获取顶点的度"""
        out_degree = self.get_out_degree(vertex)
        in_degree = self.get_in_degree(vertex)
        # 顶点存在的前提下
        if self.__vertex_is_exist(vertex):
            # 无向图
            if self.graph_type == 1:
                degree = (out_degree + in_degree) / 2
            else:  # 有向图
                degree = out_degree + in_degree
            return degree

    def get_in_degree(self, vertex):
        """求有向图某一顶点的入度。"""
        # 需要遍历完所有邻接列表，时间复杂度较高，有时通过建立逆邻接列表实现。
        # 此处采用遍历的方法。
        in_degree = 0
        for i in range(self.__vertex_num):
            edge_node = self.adjacency_list[i].first_arc
            while edge_node is not None:
                if edge_node.index == vertex:
                    in_degree = in_degree + 1
                edge_node = edge_node.next_arc
        return in_degree

    def get_out_degree(self, vertex):
        """求有向图某一顶点的出度。"""
        out_degree = 0
        edge_node = self.adjacency_list[self.__get_vertex_index_in_list(vertex)].first_arc
        while edge_node is not None:
            out_degree = out_degree + 1
            edge_node = edge_node.next_arc
        return out_degree

    def add_vertex(self, index):
        """像图中添加结点。"""
        # 判断要添加的结点是否已存在
        if self.__vertex_is_exist(index):
            return
        else:
            self.adjacency_list.append(Vertex(index))
            self.__vertex_num = self.__vertex_num + 1  # 图的结点数增加1

    def add_edge(self, start, end, weight=1):
        """
        添加边或弧。

        :param start: 边的起点编号。
        :param end: 边的终点编号。
        :param weight: 边的权重值，默认为1.
        :return:
        """
        # 判断结点是否存在，若不存在，则向图中添加该结点
        if not self.__vertex_is_exist(start):
            self.add_vertex(start)
        if not self.__vertex_is_exist(end):
            self.add_vertex(end)
        # 无向图
        if self.graph_type == 1:
            edge_node = EdgeNode(end, weight)
            # 向头结点的邻接列表中插入边结点
            self.__insert_edge_node(self.__get_vertex_index_in_list(start), edge_node)
            edge_node_inv = EdgeNode(start, weight)
            self.__insert_edge_node(self.__get_vertex_index_in_list(end), edge_node_inv)
        # 有向图
        if self.graph_type == 0:
            edge_node = EdgeNode(end, weight)
            # 向头结点的邻接列表中插入边结点
            self.__insert_edge_node(self.__get_vertex_index_in_list(start), edge_node)

    def display_algraph(self):
        """输出图的邻接列表。"""
        print("邻接列表为：")
        for i in range(self.__vertex_num):
            output = "   结点" + str(self.adjacency_list[i].index)
            edge_node = self.adjacency_list[i].first_arc
            # 邻接列表不为空，则输出
            while edge_node is not None:
                output = output + "->" + str(edge_node.index)
                edge_node = edge_node.next_arc
            print(output)


if __name__ == '__main__':
    adjacency_matrix = [
        [0, 1, 0, 5, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 4, 7],
        [0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0],
    ]
    # 构建图的邻接列表结构
    algraph = ALGraph(adjacency_matrix)
    # 输出图的邻接列表
    algraph.display_algraph()
    # 测试：添加结点
    algraph.add_vertex(6)
    # 测试：添加边
    algraph.add_edge(6, 5, 2)
    # 输出图的邻接列表
    algraph.display_algraph()
