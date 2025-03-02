'''基于邻接矩阵实现无向图'''

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, print_matrix


'''邻接矩阵实现无向图'''
class GraphAdjaMat:
    # 构造方法
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        # 顶点列表，元素代表顶点值，索引代表顶点索引
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应顶点索引
        self.adj_mat: list[list[int]] = []
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        for e in edges:
            self.add_edge(e[0], e[1])
        
    # 获取顶点数量
    def size(self) -> int:
        return len(self.vertices)
    
    # 添加顶点
    def add_vertex(self, val: int):
        n = self.size()
        # 向顶点列表中添加新的顶点的值
        self.vertices.append(val)
        # 在邻接矩阵中添加一行
        new_row = [0] * n
        self.adj_mat.append(new_row)
        # 在邻接矩阵中添加一列
        for row in self.adj_mat:
            row.append(0)

    # 删除顶点
    def remove_vertex(self, index: int):
        if index >= self.size():
            raise IndexError()
        # 在顶点列表中移除索引 index 的顶点
        self.vertices.pop(index)
        # 在邻接矩阵中删除索引 index 的行
        self.adj_mat.pop(index)
        # 在邻接矩阵中删除索引 index 的列
        for row in self.adj_mat:
            row.pop(index)
        
    # 添加边
    def add_edge(self, i: int, j: int):
        # 参数 i , j 对应顶点 vertices 元素索引
        # 如果索引越界或者相等则抛出异常
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # 在无向图中，邻接矩阵关于主对角线对称，即满足 （i, j) == (j, i)
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
    
    # 删除边
    def remove_edge(self, i: int, j: int):
        # 参数 i , j 对应顶点 vertices 元素索引
        # 如果索引越界或者相等则抛出异常
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # i, j 之间删除边，取对应的值为 0 即可，代表 i, j 之间无边
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    # 打印邻接矩阵
    def print(self):
        print(f'顶点列表 = {self.vertices}')
        print(f'邻接矩阵 = ')
        print_matrix(self.adj_mat)

'''Driver Code'''
if __name__ == '__main__':
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjaMat(vertices, edges)
    print(f'\n初始化后， 图为')
    graph.print()

    # 添加边
    # 顶点 1， 2 的索引分别为 0， 2
    graph.add_edge(0, 2)
    print(f'\n添加边 1-2 后，图为')
    graph.print()

    # 删除边
    graph.remove_edge(0, 1)
    print(f'\n删除边 1-3 后，图为')
    graph.print()

    # 添加顶点
    graph.add_vertex(6)
    print(f'n\添加顶点 6 后，图为')
    graph.print()

    # 删除顶点
    graph.remove_vertex(1)  # 索引 1
    print(f'\n删除顶点 3 后，图为')
    graph.print()

        
            


        