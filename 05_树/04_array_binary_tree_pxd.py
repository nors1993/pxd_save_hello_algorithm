'''二叉树的数组表示'''

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree, print_heap

'''数组表示下的二叉树类'''
class ArrayBinaryTree:
    # 构造方法，初始化
    # def __init__(self, arr: int | None):
    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)
    
    # 列表容量
    def size(self) -> int:
        return len(self._tree)
    
    # 获取索引为 i 节点的值
    def val(self, i: int) -> int:
        # 如果索引越界，则返回 None,代表空位
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]
    
    # 获取索引为 i 节点的左子节点的索引
    def left(self, i: int) -> int | None:
        return 2 * i + 1
    
    # 获取索引为 i 节点的右子节点的索引
    def right(self, i : int) -> int | None:
        return 2 * i + 2
    
    # 获取索引为 i 节点的父节点索引
    def parent(self, i: int) -> int | None:
        return (i - 1) // 2
    
    '''广度优先遍历 bfs（层序遍历）'''
    def level_order(self) -> list[int]:
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    
    '''深度优先遍历'''
    def dfs(self, i: int, order: str):
        if self.val(i) is None:
            return 
        # 前序遍历
        if order == 'pre':
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)

        # 中序遍历
        if order == 'in':
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)

        # 后续遍历
        if  order == 'post':
            self.res.append(self.val(i))
    
    # 前序遍历
    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order='pre')
        return self.res
    
    # 中序遍历
    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order='in')
        return self.res
    
    # 后续遍历
    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order='post')
        return self.res

'''Driver Code'''
if __name__ == '__main__':
    # 使用数组初始化二叉树
    arr = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
    root = list_to_tree(arr)
    print(f'\n初始化二叉树\n')
    print(f'二叉树的数组表示：')
    print(arr)
    print(f'二叉树的链表表示：')
    print_tree(root)
    
    # 数组表示下的二叉树类
    abt = ArrayBinaryTree(arr)  # 实例化

    # 访问节点
    i = 1
    l, r, p = abt.left(i), abt.right(i), abt.parent(i)
    print(f'\n当前节点的索引为 {i}，值为 {abt.val(i)}')
    print(f'左子节点的索引为 {l}，值为 {abt.val(l)}')
    print(f'右子节点的索引为 {r}，值为 {abt.val(r)}')
    print(f'父子节点的索引为 {p}，值为 {abt.val(p)}')

    # 遍历树
    res = abt.level_order()
    print(f'层序遍历为：{res}')
    res = abt.pre_order()
    print(f'前序遍历为：{res}')
    res = abt.in_order()
    print(f'中序遍历为：{res}')
    res = abt.post_order()
    print(f'后序遍历为：{res}')



        




