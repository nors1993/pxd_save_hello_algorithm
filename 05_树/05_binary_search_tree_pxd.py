'''
二叉搜索树：
1）对于根节点，左子树中所有节点的值 < 根节点的值 < 右子树中所有节点的值
2）对应任意节点，其左、右子树也是二叉搜索树，满足1）的条件
'''

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree

'''二叉搜索树类'''
class BinarySearchTree:
    # 构造函数，初始化树
    def __init__(self, root: TreeNode | None):
        self._root = root
    
    # 获取二叉树的根节点
    def get_root(self) -> TreeNode | None:
        return self._root
    