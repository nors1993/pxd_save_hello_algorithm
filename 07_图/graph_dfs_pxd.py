'''图的深度优先遍历 DFS'''
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vets_to_vals, vals_to_vets
from graph_adjacency_list_pxd import GraphAdjList

'''深度优先遍历辅助函数'''
def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    res.append(vet)  # 记录访问顶点
    visited.add(vet)  # 标记该顶点已被访问
    # 遍历该顶点的所有邻接顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue
        dfs(graph, visited, res, adjVet)

# 深度优先遍历
def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res =[]
    # 哈希表，用于记录已被访问过的顶点
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res

"""Driver Code"""
if __name__ == '__main__':
    # 初始化无向图
    v = vals_to_vets([0, 1, 2, 3, 4, 5, 6])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[5]],
        [v[4], v[5]],
        [v[5], v[6]],
    ]
    graph = GraphAdjList(edges)
    print(f'\n初始化后，图为')
    graph.print()

    # 深度优先遍历
    res = graph_dfs(graph, v[0])
    print(f'\n深度优先遍历（DFS)顶点序列为')
    print(vets_to_vals(res))
