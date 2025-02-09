#双向链表节点
class ListNode:
    # 构造方法
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None  # 后继节点
        self.prev: ListNode | None = None  # 前驱节点

# 基于双向链表实现的双向队列
class LinkedListDeque:
    # 构造方法
    def __init__(self):
        self._front: ListNode | None = None  # 头节点 front
        self._rear: ListNode | None = None  # 尾节点
        self._size: int = 0  # 双向队列的长度


    # 获取双向队列的长度
    def size(self) -> int:
        return self._size
    
    # 判断双向队列是否为空
    def is_empty(self) -> bool:
        return self.size() == 0
    
    '''入队操作'''
    def push(self, num: int, is_front: bool):
        node = ListNode(num)
        # 如果链表为空，则令 front 和 rear 都指向 node
        if self.is_empty():
            self._front = self._rear = node
        # 队首入队操作
        elif is_front:
            # 将 node 添加至链表头部
            self._front.prev = node
            node.next = self._front
            self._front = node  # 更新头节点
        # 队尾入队操作
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node  # 更新尾节点
        self._size += 1  # 更新队列长度
    
    # 队首入队
    def push_first(self, num: int):
        self.push(num, True)
    
    # 队尾入队
    def push_last(self, num: int):
        self.push(num, False)
    
    '''出队操作'''
    def pop(self, is_front: bool) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        # 队首出队操作
        if self.is_front:
            val: int = self._front.val  # 暂存头节点值
            # 删除头节点
            fnext: ListNode | None = self._front.next
            if fnext != None:
                fnext.prev = None
                self._front.next = None  # 断开原头节点与下一个节点的连接
            self._front = fnext  # 更新头节点
        # 队尾出队操作
        else:
            val: int = self._rear.val  # 暂存尾节点值
            # 删除尾节点
            rprev: ListNode | None = self._rear.prev
            if rprev != None:
                rprev.next = None
                self._rear.prev = None  # 断开原尾节点与上一个节点的连接
            self._rear = rprev  # 更新尾节点
        self._size -= 1  # 更新队列长度
        return val
    
    # 队首出队
    def pop_first(self) -> int:
        return self.pop(True)

    # 队尾出队
    def pop_last(self) -> int:
        return self.pop(False)
    
    # 访问队首元素
    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._front.val
        
    # 访问队尾元素
    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._rear.val
    
    # 返回数组用于打印
    def to_array(self) -> list[int]:
        node = self._front
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res

'''Driver Code'''
if __name__ == '__main__':
    # 初始化双向队列
    deque = LinkedListDeque()
    deque.push_last(2)
    deque.push_last(3)
    deque.push_first(1)
    print(f'双向队列 deque = {deque.to_array()}')

    # 访问元素
    peek_first: int = deque.peek_first()
    peek_last: int = deque.peek_last()
    print(f'队首元素 peek_first = {peek_first}, 队尾元素 peek_last = {peek_last}')
    
    # 元素入队
    deque.push_last(4)
    print(f'元素 4 入队后 deque = {deque.to_array()}')
    deque.push_first(5)
    print(f'元素 5 入队后 deque = {deque.to_array()}')

    # 获取双向队列的长度
    size: int = deque.size()
    print(f'双向队列长度 size = {size}')

    # 判断双向队列是否为空
    is_empty: bool = deque.is_empty()
    print(f'双向队列是否为空 = {is_empty}')






