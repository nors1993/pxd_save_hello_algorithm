''' AVL 树：即平衡二叉搜索树，既具备二叉搜索树的性质，又具备平衡二叉树的性质
'''

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree

'''AVL 树'''
class AVLTree:
    # 构造方法
    def __init__(self):
        self._root = None
    
    # 获取二叉树根节点
    def get_root(self) -> TreeNode | None:
        return self._root
    
    # 获取二叉树高度
    def height(self, node: TreeNode | None) -> int:
        # 空节点高度为 -1 ，叶节点高度为 0 
        if node is not None:
            return node.height
        return -1
    
    # 更新节点高度
    def update_height(self, node: TreeNode | None):
        # 节点高度等于最高子树高度 + 1
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    # 获取平衡因子
    def balance_factor(self, node: TreeNode | None) -> int:
        # 空节点平衡因子为 0 
        if node is None:
            return 0 
        # 平衡因子 = 左子树高度 - 右子树高度
        return self.height(node.left) - self.height(node.right)
    
    '''右旋操作(子节点在失衡节点的左侧)'''
    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
        child = node.left
        grand_child = child.right  # child 有右子节点时
        # 以 child 为原点，将 node 向右旋转
        child.right = node
        node.left = grand_child  # 右旋后将 grand_child 作为旋转后 node 的左子节点
        # 更新节点高度
        self.update_height(node)  # 旋转后原失衡节点的高度
        self.update_height(child)  # 旋转后根节点的高度
        # 返回旋转后子树的根节点
        return child
    
    '''左旋操作（子节点在失衡节点的右侧）,操作与右旋对称，代码中将 right 换为 left，将 left 换为 right 即可'''
    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
        child = node.right
        grand_child = child.left
        # 以 child 为原点，将 node 向左旋转
        child.left = node
        node.right = grand_child  # 左旋后将 grand_child 作为旋转后 node 的右子节点
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)
        # 返回旋转后子树的根节点
        return child
    
    '''执行旋转操作，使该子树重新恢复平衡'''
    def rotate(self, node: TreeNode | None) -> TreeNode | None:
        # 获取节点 node 的平衡因子
        balance_factor = self.balance_factor(node)
        # 对于《左偏树》 
        if balance_factor > 1:
            if self.balance_factor(node.left) >= 0:
                # 右旋
                return self.right_rotate(node)
            else:
                # 先左旋后右旋
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 对于《右偏树》
        elif balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                # 左旋
                return self.left_rotate(node)
            else:
                # 先右旋后左旋
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # 对于已经平衡的树，无需旋转，直接返回
        return node
    
    # 插入节点
    def insert(self, val):
        self._root = self.insert_helper(self._root, val)
    
    # 递归插入节点（辅助方法）
    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        # 1、查找插入位置并插入节点
        if val < node.val:  # 插入位置在左侧
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:  # 插入位置在右侧
            node.right = self.insert_helper(node.right, val)
        else:  # 重复节点不插入，直接返回
            return node
        # 更新节点高度
        self.update_height(node)
        # 2、执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)
    
    # 删除节点
    def remove(self, val: int):
        self._root = self.remove_helper(self._root, val)
    
    # 递归删除节点（辅助方法）
    def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return None
        # 1、查找节点并删除
        if val < node.val:  # 待删除节点在左侧
            node.left = self.remove_helper(node.left, val)
        elif val > node.val:  # 待删除节点在右侧
            node.right = self.remove_helper(node.right, val)
        else:  # 如果待删除节点是当前节点
            if node.left is None or node.right is None:
                child = node.left or node.right
                # 子节点数量 = 0，直接删除 node 并返回
                if child is None:
                    return None
                # 子节点数量 = 1，用子节点覆盖 node 进行删除
                else:
                    node = child
            else:  # 子节点数量 = 2， 则将中序遍历的下个节点删除，并用该节点替换当前节点
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.right = self.remove_helper(node.right, temp.val)
                node.val = temp.val
        # 更新节点高度
        self.update_height(node)
        # 2、执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)
    
    # 查找节点
    def search(self, val: int) -> TreeNode | None:
        cur = self._root  # 初始化查找节点，从根节点开始
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < val:
                cur = cur.right
            # 目标节点在 cur 的左子树中
            elif cur.val > val:
                cur = cur.left
            # 重复节点，直接跳出循环
            else:
                break
        return cur

'''Driver Code'''
if __name__ == '__main__':

    def test_insert(tree: AVLTree, val: int):
        tree.insert(val)
        print(f'\n插入节点 {val} 后，AVL树为 ')
        print_tree(tree.get_root())

    def test_remove(tree: AVLTree, val: int):
        tree.remove(val)
        print(f'\n删除节点 {val}后，AVL树为')
        print_tree(tree.get_root())

    # 初始化空 AVL 树
    avl_tree = AVLTree()

    # 插入节点
    for val in [1, 2, 3, 4, 5, 8, 7, 9, 10, 6]:
        test_insert(avl_tree, val)
    
    # 插入重复节点(关注插入节点后，AVL 树是如何保持平衡的)
    test_insert(avl_tree, 7)

    # 删除节点
    test_remove(avl_tree, 8)  # 删除度为 0 的节点
    test_remove(avl_tree, 5)  # 删除度为 1 的节点
    test_remove(avl_tree, 4)  # 删除度为 2 的节点

    result_node = avl_tree.search(7)
    print(f"\n查找到的节点对象为 {result_node}，节点值 = {result_node.val}")





    
                















