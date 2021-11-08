# -*- coding: utf-8 -*-
# author：57213
# description：图存储结构————邻接列表

from Graph import Vertex
from Graph import EdgeNode


# 图——邻接列表存储结构
class ALGraph(object):
    def __init__(self, matrix, graph_type=0 | 1):
        """
        构造函数：使用邻接矩阵生成图的邻接表。

        :param matrix: 邻接矩阵
        :param graph_type: 图的类型，1：无向图（默认）；0：有向图
        """
        self.__graph_type = graph_type
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
            self.adjacency_list.append(Vertex.Vertex(i))
        # 根据邻接矩阵建立邻接列表
        for row in range(self.__vertex_num):
            for column in range(self.__vertex_num):
                # 跳过对邻接矩阵对角线元素的操作
                if row == column:
                    continue
                # 邻接矩阵中不为0和无穷大处，表示二者间有边
                if matrix[row][column] != 0 and matrix[row][column] != float('inf'):
                    # 无向图
                    if self.__graph_type == 1:
                        edge_node = EdgeNode.EdgeNode(column, matrix[row][column])
                        self.__insert_edge_node(row, edge_node)  # 向某头结点的邻接列表中插入边结点
                        edge_node_inv = EdgeNode.EdgeNode(row, matrix[row][column])
                        self.__insert_edge_node(column, edge_node_inv)  # 向某头结点的邻接列表中插入边结点
                    # 有向图
                    if self.__graph_type == 0:
                        edge_node = EdgeNode.EdgeNode(column, matrix[row][column])
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

    def get_vertex_index_in_list(self, vertex_index):
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
            index = self.get_vertex_index_in_list(start)
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
            if self.__graph_type == 1:
                degree = (out_degree + in_degree) // 2
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
        # 即相应邻接“链表”中边结点的个数
        out_degree = 0
        edge_node = self.adjacency_list[self.get_vertex_index_in_list(vertex)].first_arc
        while edge_node is not None:
            out_degree = out_degree + 1
            edge_node = edge_node.next_arc
        return out_degree

    def add_vertex(self, index):
        """向图中添加结点。"""
        # 判断要添加的结点是否已存在
        if self.__vertex_is_exist(index):
            print("结点{}已存在！".format(index))
            return
        else:
            self.adjacency_list.append(Vertex.Vertex(index))
            self.__vertex_num = self.__vertex_num + 1  # 图的结点数增加1
            print("成功添加结点{}！".format(index))

    def delete_vertex(self, index):
        """
        删除顶点及其相关边或弧。

        :param index: 要删除的顶点编号
        """
        # 待删除顶点不存在，不做任何处理
        if not self.__vertex_is_exist(index):
            print("结点{}不存在！".format(index))
            return
        n = self.get_vertex_index_in_list(index)  # 记录结点在头结点表中的索引值
        temp = self.adjacency_list.pop(n)  # 删除相应单链表
        self.__vertex_num = self.__vertex_num - 1  # 图结点数减少1
        # 无向图，利用temp在其他结点的邻接链表中删除相关边结点
        if self.__graph_type == 1:
            edge_node = temp.first_arc  # 记录与要删除的结点间有边的结点
            while edge_node is not None:
                edge_node_index = edge_node.index  # 与要删除的结点间有边的结点的编号
                self.remove_edge_node(edge_node_index, index)
                edge_node = edge_node.next_arc
        # 有向图，需要额外遍历其他结点的邻接链表并删除相关边结点
        if self.__graph_type == 0:
            for i in range(self.__vertex_num):
                edge_node_index = self.adjacency_list[i].index
                self.remove_edge_node(edge_node_index, index)
        print("成功删除结点{}及相关边！".format(index))

    def remove_edge_node(self, edge_node_index, remove_index):
        """
        从头结点的邻接链表中删除相关边结点。

        :param edge_node_index: 与要删除的结点间有边的结点的编号
        :param remove_index:  要删除的结点编号
        """
        n = self.get_vertex_index_in_list(edge_node_index)
        pre = self.adjacency_list[n]  # 头结点
        node = pre.first_arc  # 与头结点最近的边结点，必不为None
        flag = 0  # 用于标记目前操作节点前一结点为头结点
        while node is not None:
            if flag == 0:
                if node.index == remove_index:
                    pre.first_arc = node.next_arc
                    return
                pre = pre.first_arc
                node = node.next_arc
                flag = 1
            else:
                if node.index == remove_index:
                    pre.next_arc = node.next_arc
                    return
                pre = pre.next_arc
                node = node.next_arc

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
        if self.__graph_type == 1:
            edge_node = EdgeNode.EdgeNode(end, weight)
            # 向头结点的邻接列表中插入边结点
            self.__insert_edge_node(self.get_vertex_index_in_list(start), edge_node)
            edge_node_inv = EdgeNode.EdgeNode(start, weight)
            self.__insert_edge_node(self.get_vertex_index_in_list(end), edge_node_inv)
            print("成功添加边{0}--{1}".format(start, end))
        # 有向图
        if self.__graph_type == 0:
            edge_node = EdgeNode.EdgeNode(end, weight)
            # 向头结点的邻接列表中插入边结点
            self.__insert_edge_node(self.get_vertex_index_in_list(start), edge_node)
            print("成功添加边{0}->{1}".format(start, end))

    def display_algraph(self):
        """输出图的邻接列表。"""
        print("图的邻接列表为：")
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

    # region # 无向图测试
    print("----------------无向图测试----------------")
    # 构建图的邻接列表结构
    non_dir_algraph = ALGraph(adjacency_matrix)
    # 输出图的邻接列表
    print("----原邻接列表----")
    non_dir_algraph.display_algraph()
    print("图中顶点数为：", non_dir_algraph.get_vertex_num())
    # 测试：添加结点
    non_dir_algraph.add_vertex(6)  # 添加不存在的点
    non_dir_algraph.add_vertex(2)  # 添加已有点
    # 测试：添加边
    non_dir_algraph.add_edge(6, 5, 2)  # （边的一个结点为之前图中不存在的）
    non_dir_algraph.add_edge(0, 5, 8)
    print("----添加结点及边后----")
    print("图中顶点数为：", non_dir_algraph.get_vertex_num())
    # 输出有向图的邻接列表
    non_dir_algraph.display_algraph()
    print("----删除一个结点后----")
    # 删除顶点
    non_dir_algraph.delete_vertex(1)
    print("图中顶点数为：", non_dir_algraph.get_vertex_num())
    # 输出有向图的邻接列表
    non_dir_algraph.display_algraph()
    # 测试：边权值获取
    print("边34的权值：", non_dir_algraph.get_edge_value(3, 4))
    # 测试：顶点度获取
    print("顶点2的度：", non_dir_algraph.get_vertex_degree(2))
    # endregion

    # region # 有向图测试
    print("----------------有向图测试----------------")
    dir_algraph = ALGraph(adjacency_matrix, 0)  # 构建图的邻接列表
    print("----原邻接列表----")
    dir_algraph.display_algraph()  # 输出邻接列表
    # 测试：顶点的度
    print("顶点2的度：", dir_algraph.get_vertex_degree(2))
    print("顶点2的入度：", dir_algraph.get_in_degree(2))
    print("顶点2的出度：", dir_algraph.get_out_degree(2))
    dir_algraph.add_edge(9, 2, 2)  # 添加边
    print("----添加边后----")
    dir_algraph.display_algraph()  # 输出邻接列表
    # 测试：顶点的度
    print("顶点2的度：", dir_algraph.get_vertex_degree(2))
    print("顶点2的入度：", dir_algraph.get_in_degree(2))
    print("顶点2的出度：", dir_algraph.get_out_degree(2))
    print("----删除结点后----")
    dir_algraph.delete_vertex(2)
    dir_algraph.display_algraph()  # 输出邻接列表
    # endregion
