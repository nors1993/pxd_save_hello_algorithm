'''二叉树的广度优先搜索（层序遍历）'''

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree
from collections import deque

'''层序遍历'''
def level_order(root: TreeNode | None) -> list[int]:
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res

'''Driver Code 测试代码'''
if __name__ == '__main__':
    # 初始化二叉树，使用数组直接生成二叉树
    root: TreeNode = list_to_tree (arr=[1, 2, 3, 4, 5, 6, 7])
    print(f'\n初始化二叉树\n')
    print_tree(root)

    # 层序遍历
    res: list[int] = level_order(root)
    print(f'层序遍历的节点打印序列 = {res}\n')
