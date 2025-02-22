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
    # def __init__(self, root: TreeNode | None = None):
    #     self._root = root
    def __init__(self):
        self._root = None
    
    # 获取二叉树的根节点
    def get_root(self) -> TreeNode | None:
        return self._root
    
    # 查找节点
    def search(self, num: int) -> int:
        cur = self._root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            # 目标节点在 cur 的左子树中
            if cur.val > num:
                cur = cur.left
            else:
                break  # 二叉搜索树中不存在相等的重复节点
        return cur
    
    # 插入节点
    def insert(self, num: int):
        # 如果树为空，则初始化根节点
        if self._root is None:
            self._root = TreeNode(num)
            return
        # 循环查找插入位置，越过叶节点后（找到插入位置）跳出
        cur, pre = self._root, None  # 初始化，pre 为当前节点的父节点
        while cur is not None:
            # 找到重复节点，直接返回（二叉树中不存在重复节点）
            if cur.val == num:
                return
            pre = cur  # 记录当前节点为下一个循环的父节点
            # 插入位置在 cur 节点的右子树中，移动当前节点 cur 指向下一个右节点
            if cur.val < num:
                cur = cur.right
            # 插入位置在 cur 节点的左子树中，移动当前节点 cur 指向下一个左子节点
            else:
                cur = cur.left
        # 直到上述循环找到插入节点的位置（cur 指向 None），在 None 出插入节点
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node
    
    # 删除节点
    def remove(self, num: int):
        # 如果树为空，直接提前返回
        if self._root is None:
            return
        # 循环查找待删除节点，越过叶节点后跳出
        cur, pre = self._root, None  # 初始化， pre 为当前根节点 cur 的父节点
        while cur is not None:
            # 找到待删除节点，跳出循环
            if cur.val == num:
                break
            pre = cur  # 记录当前节点为下一个循环的父节点
            # 待删除节点在当前节点 cur 的右子树中,将当前节点指向下一个右子节点
            if cur.val < num:
                cur = cur.right
            # 待删除节点在当前节点 cur 的左子树中，将当前节点指向下一个左子节点
            if cur.val > num:
                cur = cur.left
        
        # 若无待删除节点，则直接返回
        if cur is None:
            return
        
        # 找到待删除节点，对节点进行删除，并用满足二叉搜索树性质的子节点覆盖当前已删除节点位置
        # 子节点数量为 0 或 1
        if cur.left is None or cur.right is None:
            # 该节点的子节点数量为 0 或 1时，子节点的为 null 或 左/右子节点
            child = cur.left or cur.right
            # 删除节点 cur
            # 如果删除的不是根节点
            if cur != self._root:
                if pre.left == cur:  # 如果 cur 是父节点的左子节点
                    pre.left = child   # 使用 child 替换掉 cur,即删除了 cur
                else:
                    pre.right = child
            else:
                # 如果待删除节点为根节点，则重新指定根节点
                self._root = child
        # 子节点数量为 2，删除节点后，需要重新调整二叉树，满足二叉树搜索树的性质，即使用待删除节点的左子树中的最大值或者右子树中的最小值调整到该节点位置，此处使用右子树中的最小值（使用中序遍历）
        else:
            # 获取中序遍历中 cur 的下一个节点(比 cur 大的最小节点，即右子树的最小节点，右子树的左子节点为最小节点）
            tmp: TreeNode = cur.right  # 当前节点视为根节点，中序遍历下一个节点也就是右侧节点
            while tmp.left is not None:
                tmp = tmp.left
            # 递归删除节点 tmp
            self.remove(tmp.val)
            # 用 tmp 覆盖 cur
            cur.val = tmp.val

"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉搜索树
    
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    bst = BinarySearchTree()
    # 请注意，不同的插入顺序会生成不同的二叉树，该序列可以生成一个完美二叉树
    for num in nums:
        bst.insert(num)
    print("\n初始化的二叉树为\n")
    print_tree(bst.get_root())

    # 查找节点
    node = bst.search(7)
    print("\n查找到的节点对象为: {}，节点值 = {}".format(node, node.val))

    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后，二叉树为\n")
    print_tree(bst.get_root())

    # 删除节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(2)
    print("\n删除节点 2 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(4)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.get_root())