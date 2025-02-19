'''
二叉树的深度优先搜索：
前序遍历、中序遍历、后序遍历

'''
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree,print_tree

'''前序遍历'''
def pre_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

'''中序遍历'''
def in_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

'''后序遍历'''
def post_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    in_order(root=root.left)
    in_order(root=root.right)
    res.append(root.val)

'''Driver Code'''
if __name__ == '__main__':
    # 初始化二叉树，借助从数组直接生成二叉树
    root = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7])
    print(f'\n初始化二叉树\n')
    print_tree(root)
    
    # 前序遍历
    res = []
    pre_order(root)
    print(f'\n前序遍历的节点打印序列 = {res}\n')

    # 中序遍历
    res.clear()
    in_order(root)
    print(f'\n中序遍历的节点打印序列 = {res}\n')

    # 后序遍历
    res.clear()
    post_order(root)
    print(f'\n后序遍历的节点打印序列 = {res}\n')

    


