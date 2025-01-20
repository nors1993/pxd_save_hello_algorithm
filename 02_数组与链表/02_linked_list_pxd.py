'''
数组和列表的区别：
列表 是一种灵活且功能丰富的数据结构，适合用于存储各种数据类型。
数组 提供更高的性能，适合存储和处理相同类型的数值数据。

'''

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent)) # 为了导入上上级目录的 modules
from modules import ListNode, print_linked_list

def insert (n0: ListNode, P: ListNode):
    '''在链表的结点 n0 之后插入节点 P'''
    n1 = n0.next
    n0.next = P
    P.next = n1

def remove(n0: ListNode):
    '''删除链表的节点 n0 之后的首个节点'''
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1
    P = None  # 无需清除节点亦可，此处清除更标准些

def access(head: ListNode, index: int) -> ListNode | None:
    '''访问链表中索引为 index 的节点'''
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head: ListNode, target: int) -> int:
    '''在链表中查找值为 target 的首个节点'''
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1     

'''Driver Code'''
if __name__ == '__main__':
    # 初始化链表
    # 初始化各个节点
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    # 构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print('初始化的链表为：')
    print_linked_list(n0)

    # 插入节点
    p = ListNode(0)
    insert(n0, p)
    print('插入节点后的链表为：')
    print_linked_list(n0)

    # 删除节点
    remove(n2)
    print('删除节点后的链表为：')
    print_linked_list(n0)

    # 访问节点
    node: ListNode = access(n0, 3)
    print(f'链表中索引 3 处的节点的值 = {node.val}')
    
    # 查找节点
    index: int = find(n1, 5)
    print('链表中值为 2 的节点的索引 = {}'.format(index))



