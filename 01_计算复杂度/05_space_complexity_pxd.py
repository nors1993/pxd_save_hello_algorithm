import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent)) # 为了导入上上级目录的 modules
from modules import ListNode, TreeNode, print_tree

def function() -> int:
    '''函数'''
    # 执行某些操作
    return 0

def constant(n: int):
    '''常数阶'''
    # 常量、变量、对象占用 O(1) 空间
    a = 0
    nums = [0] * 10000
    node = ListNode(0) # 单链表节点
    # 循环中的变量占用 O(1) 空间
    for _ in range(n):
        c = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()

def linear(n: int):
    '''线性阶'''
    # 长度为 n 的列表占用 O(n) 空间
    nums = [0] * n
    # 长度为 n 的哈希表占用 O(n) 空间
    #hmap = dict[int, str()]()
    hamap: dict[int, str] = {}
    for i in range(n):
        hamap[i] = str(i)

def linear_recur(n: int):
    '''线性阶（递归实现）'''
    print("递归 n =", n)
    if n == 1:
        return
    linear_recur(n - 1)

def quadratic(n: int):
    '''平方阶'''
    # 二维列表占用 O(n^2) 空间
    num_matrix = [[0] * n for _ in range(n)]

def quadratic_recur(n: int) -> int:
    '''平方阶（递归实现）'''
    if n <= 0:
        return 0
    # 数组 nums 长度为 n, n-1, ..., 2, 1
    nums = [0] * n
    return quadratic_recur(n - 1)

def build_tree(n: int) -> TreeNode:
    '''指数阶（使用递归建立满二叉树）'''
    if n == 0:
        return None
    root = TreeNode(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n - 1)
    return root


if __name__ == "__main__":
    n = 4
    constant(n)  # 常数阶
    linear(n)  # 线性阶
    linear_recur(n)  # 线性阶（递归实现）
    quadratic(n)  # 平方阶
    quadratic_recur(n)  # 平方阶（递归实现）
    root = build_tree(n)  # 指数阶（建立满二叉树）
    print_tree(root)  # 打印满二叉树
    node1 = ListNode(1) 
    print(node1)  # 打印单链表节点
    


