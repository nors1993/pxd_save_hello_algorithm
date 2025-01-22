import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from modules import ListNode

class LinkedListQueue:
    '''基于链表实现的队列'''

    def __init__(self):
        '''构造方法'''
        self._front: ListNode | None = None  # 头节点 front
        self._rear: ListNode | None = None  # 尾节点 rear
        self._size: int = 0

    # 获取队列长度
    def size(self) -> int:
        return self._size
    
    # 判断队列是否为空
    def is_empty(self) -> bool:
        return not self._front
    
    # 入队
    def push(self, num: int):
        #在尾节点增加 num
        node = ListNode(num)
        # 如果队列为空，则令头、尾节点都指向该节点
        if self._front is None:
            self._front = node
            self._rear = node
        # 如果队列不为空，则将该节点添加到队尾
        else:
            self._rear.next = node
            self._rear = node  # 更新尾节点 
        self._size += 1
    
    # 出队
    def pop(self) -> int:
        num = self.peek()
        # 删除队首节点
        self._front = self._front.next
        self._size -= 1
        return num
    
    # 访问队首元素
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
    
    # 转化为列表用于打印
    def to_list(self) -> list[int]:
        queue = []
        tem = self._front
        while tem:
            queue.append(tem.val)
            tem = tem.next
        return queue
    
if __name__ =='__main__':
    # 初始化队列
    queue = LinkedListQueue()

    # 元素入队
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(f'队列 queue = {queue.to_list()}')

    # 访问队首元素
    peek: int = queue.peek()
    print(f'队首元素 front = {peek}')

    # 元素出队
    pop: int = queue.pop()
    print(f'出队元素 pop = {pop}')
    print(f'出队后的队列 queue = {queue.to_list()}')

    # 获取队列长度
    size: int = queue.size()
    print(f'队列长度 size = {size}')
    
    # 判断是否为空
    is_empty: bool = queue.is_empty()
    print(f'队列是否为空 = {is_empty}')