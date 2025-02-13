import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree

'''初始化二叉树'''
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)

# 构建节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
print(f'\n初始化二叉树\n')
print_tree(n1)

# 插入节点
P = TreeNode(0)
# 在 n1 -> n2 之间插入节点 P
n1.left = P
P.left = n2
print(f'\n插入节点 P 后\n')
print_tree(n1)

# 删除节点
n1.left = n2
print(f'\n删除节点 P 后\n')
print_tree(n1)