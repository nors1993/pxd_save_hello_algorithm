import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import ListNode

class LinkedListStack:
    '''基于链表实现栈'''
    
    def __init__(self):
        '''构造方法'''
        self._peek: ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        '''获取栈的长度'''
        return self._size
    
    def is_empty(self) -> bool:
        '''判断栈是否为空'''
        return not self._peek
    
    def push(self, val: int):
        '''入栈'''
        node = ListNode(val)
        node.next = self._peek
        self._peek = node  # 更新栈顶元素
        self._size += 1

    def pop(self):
        '''出栈'''
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('栈为空')
        return self._peek.val
    
    def to_list(self) -> list[int]:
        '''转化为列表用于打印'''
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
    
if __name__ == '__main__':
    # 初始化栈
    stack = LinkedListStack()

    # 元素入栈
    stack.push(1)
    stack.push(2)
    stack.push(8)
    stack.push(4)
    stack.push(5)
    print(f'栈 stack = {stack.to_list()}')
 
    # 访问栈顶元素
    peek: int = stack.peek()
    print(f'栈顶元素 peek = {peek}')

    # 元素出栈
    pop: int = stack.pop()
    print(f'出栈元素 pop = {pop}')
    print(f'出栈后 stack = {stack.to_list()}')

    # 获取栈的长度
    size: int = stack.size()
    print(f'栈的长度 size = {size}')

    # 判断是否为空
    is_empty: bool = stack.is_empty() 
    print(f'栈是否为空 = {is_empty}')


