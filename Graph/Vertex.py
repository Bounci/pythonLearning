# -*- coding: utf-8 -*-
# author：Deng
# description：邻接列表 ———— 头结点类
# 邻接表图结构存储————头结点类

class Vertex(object):
    def __init__(self, index):
        """构造函数：初始化头结点。"""
        self.index = index  # 初始化头结点编号
        self.first_arc = None  # 初始化头结点的第一个边结点为None，表示头结点与其他结点间无边（弧）


if __name__ == '__main__':
    pass
