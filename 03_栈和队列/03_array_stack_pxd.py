class ArrayStack:
    '基于数组实现的栈'
    def __init__(self):
        '构造方法'
        self._stack: list[int] = []
    
    def size(self) -> int:
        '获取栈的长度'
        return len(self._stack)
    
    # 判断栈是否为空
    def is_empty(self) -> bool:
        return self._stack == []
    
    # 入栈
    def push(self, item: int):
        return self._stack.append(item)
    
    # 出栈
    def pop(self):
        if self.is_empty():
            raise IndexError('栈为空')
        return self._stack.pop()
    
    # 访问栈顶元素
    def peek(self):
        if self.is_empty():
            raise IndexError('栈为空')
        return self._stack[-1]
    
    # 返回列表用于打印
    def to_list(self) -> list[int]:
        return self._stack

def is_empty(stack: ArrayStack | None):
    if stack.size()== 0:
        a_str: str = "是"
    else:
        a_str: str = "否"
    return a_str  

if  __name__ == '__main__':
    #初始化栈
    stack = ArrayStack()

    # 元素入栈
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f'栈 stack = {stack}')

    # 访问栈顶元素
    peek: int = stack.peek()
    print(f'栈顶元素 peek = {peek}')

    # 元素出栈
    pop: int = stack.pop()
    print(f'出栈的元素 pop = {pop}')
    print(f'出栈后 stack = {stack.to_list()}')

    # 获取栈额长度
    size: int = stack.size()
    print(f'栈的长度 size = {size}')

    # 判断是否为空
    # is_empty = stack.is_empty()
    # print(f'判断是否为空 = {is_empty}')
    a_str = is_empty(stack)
    print(f'判断是否为空 = {a_str}')
