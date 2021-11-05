# -*- coding: utf-8 -*-
# author：Deng
# time：2021/11/5
# description：邻接列表 ———— 边结点类

# 邻接表图结构存储————边结点类
class EdgeNode(object):
    def __init__(self, index, weight=1):
        """
        构造函数：初始化边结点。

        :param index: 边结点编号
        :param weight: 边的权重，默认为1
        """
        self.index = index  # 初始化边结点的结点编号
        self.weight = weight  # 初始化边结点与头结点间边的权重，默认为1
        self.next_arc = None  # 初始化边结点的下一个结点为None


if __name__ == '__main__':
    pass
