'''图的广度优先搜索/遍历 BFS'''
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vets_to_vals, vals_to_vets
from graph_adjacency_list_pxd import GraphAdjList
from collections import deque


'''广度优先遍历'''
def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 初始化顶点列表
    res = []
    # 哈希表，用于记录已被问过的顶点
    visited = set[Vertex]([start_vet])
    # 队列用于实现 BFS
    que = deque[Vertex]([start_vet])
    # 以顶点 vet 为起点，循环直至访问完所有顶点
    while len(que) > 0:
        vet = que.popleft()  # 队首顶点出队
        res.append(vet)  # 记录访问顶点
        # 遍历该顶点的所有邻接顶点
        for adf_vet in graph.adj_list[vet]:
            if adf_vet in visited:
                continue  # 跳过已被访问的顶点
            que.append(adf_vet)  # 只入队未访问的顶点
            visited.add(adf_vet)  # 标记该顶点已被访问
    # 返回顶点遍历序列
    return res

'''Driver Code'''
if __name__ == '__main__':
    # 初始化无向图
    v = vals_to_vets([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[1], v[4]],
        [v[2], v[5]],
        [v[3], v[4]],
        [v[3], v[6]],
        [v[4], v[5]],
        [v[4], v[7]],
        [v[5], v[8]],
        [v[6], v[7]],
        [v[7], v[8]],
        [v[7], v[9]],
    ]
    graph = GraphAdjList(edges)
    print(f'\n初始化后，图为')
    graph.print()

    # 广度优先遍历 BFS
    res = graph_bfs(graph, v[0])
    print(f'\n广度优先遍历 （BFS） 顶点序列为')
    print(vets_to_vals(res))

        


