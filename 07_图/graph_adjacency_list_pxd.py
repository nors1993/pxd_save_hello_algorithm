'''基于邻接表实现无无向图'''
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vals_to_vets

'''邻接表无向图'''
class GraphAdjList:
    # 构造方法
    def __init__(self, edges: list[list[Vertex]]):
        # 邻接表，key:顶点， value: 该顶点的所有邻接顶点
        self.adj_list = dict[Vertex, list[Vertex]]()
        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])
    
    # 获取顶点数量
    def size(self) -> int:
        return len(self.adj_list)
        
    # 添加边
    def add_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise IndexError('顶点不存在或无向图不能自环')
        # 添加边 vet1 - vet2 ，无向图需要同时在两个顶点的相邻顶点列表中添加对方
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)
    
    # 删除边
    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise IndexError('顶点不存在或无向图不能自环')
        # 删除边 vet1 - vet2 ，无向图需要同时在两个顶点的相邻顶点列表中删除对方
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
    
    # 添加顶点
    def add_vertex(self, vet: Vertex):
        # 如果顶点存在，则直接返回
        if vet in self.adj_list:
            return
        # 如果顶点不存在，在邻接表中添加一个新链表
        self.adj_list[vet] = []
    
    # 删除顶点
    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_list:
            raise IndexError()
        # 在邻接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)
        # 遍历所有其他的顶点的链表，删除所有包含 vet 的边
        for other_vertex in self.adj_list:
            if vet in self.adj_list[other_vertex]:
                self.adj_list[other_vertex].remove(vet)
        
    # 打印邻接表
    def print(self):
        print('邻接表 = ')
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f'{vertex.val}: {tmp}, ')
    
'''Driver Code'''
if __name__ == '__main__':
    # 初始化无向图
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]],
    ]
    graph = GraphAdjList(edges)
    print('\n初始化后， 图为')
    graph.print()
    
    # 添加边 1 - 2
    graph.add_edge(v[0], v[2])
    print(f'\n添加边 1 -2 后，图为')
    graph.print()

    # 删除边 1 - 3
    graph.remove_edge(v[0], v[1])
    print(f'\n删除边 1 - 3 后，图为')
    graph.print()

    # 添加顶点
    v5 = Vertex(6)
    graph.add_vertex(v5)
    print(f'\n添加顶点 6 后，图为')
    graph.print()

    # 删除顶点
    graph.remove_vertex(v[1])
    print(f'\n删除顶点 3 后， 图为')
    graph.print()
            
