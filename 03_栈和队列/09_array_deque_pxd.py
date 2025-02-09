'基于环形数组实现的双向队列'

class ArrayDeque:
    # 构造方法
    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    # 获取双向队列的容量
    def capacity(self) -> int:
        return len(self._nums)
    
    # 获取双向队列的长度
    def size(self) -> int:
        return self._size
    
    # 判单双向队列是否为空
    def is_empty(self) -> bool:
        return self._size == 0
    
    # 计算环形数组索引
    def index(self, i: int) -> int:
        # 通过取余操作实现数组首尾相连；当 i 越过数组尾部后，回到头部；当 i 越过数组头部后，回到尾部
        return (i + self.capacity()) % self.capacity()
    
    # 队首入队
    def push_first(self, num: int):
        if self._size == self.capacity():
            print('双向队列已满')
            return
        # 队首指针向左移一位；通过取余操作实现 front 越过数组头部回到尾部
        self._front = self.index(self._front - 1)
        # 将 num 添加到队首
        self._nums[self._front] = num
        self._size += 1
    
    # 队尾入队
    def push_last(self, num: int):
        if self._size == self.capacity():
            print('双向队列已满')
            return
        # 计算队尾指针，指向队尾索引 +1
        rear = self.index(self._front + self._size)
        self._nums[rear] = num
        self._size += 1
    
    # 队首出队
    def pop_first(self) -> int:
        num = self.peek_first()
        # 队首指针向后移一位
        self._front = self.index(self._front + 1)
        self._size -= 1
        return num
    
    # 队尾出队
    def pop_last(self) -> int:
        num = self.peek_last()
        self._size -= 1
        return num
    
    # 访问队首元素
    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._nums[self._front]
    
    # 访问队尾元素
    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError('双线队列为空')
        # 计算队尾元素索引
        last = self.index(self._front + self._size -1)
        return self._nums[last]
    
    # 返回数组用于打印
    def to_array(self) -> list[int]:
        # 仅转换有效长度范围内的列表元素
        res = []
        for i in range(self._size):
            res.append(self._nums[self.index(self._front + i)])
        return res

'''Driver Code'''    
if __name__ == '__main__':
    # 初始化双向队列
    deque = ArrayDeque(10)
    deque.push_first(2)
    deque.push_last(3)
    deque.push_first(1)
    print(f'双向队列 deque = {deque.to_array()}')

    # 访问元素
    peek_first: int = deque.peek_first()
    peek_last: int = deque.peek_last()
    print(f'双向队列首元素 peek_first = {peek_first}, 队尾元素 peek_last = {peek_last}')
    
    # 元素入队
    deque.push_first(4)
    print(f'入队元素 4 后  deque = {deque.to_array()}')
    deque.push_last(5)
    print(f'入队元素 5 后 deque = {deque.to_array()}')

    # 元素出队
    pop_first: int =  deque.pop_first()
    print(f'出队元素 pop_first = {pop_first}, 出队后 deque = {deque.to_array()}')
    pop_last: int = deque.pop_last()
    print(f'出队元素 pop_last = {pop_last}, 出队后 deque = {deque.to_array()}')

    # 获取双向队列的长度
    size: int = deque.size()
    print(f'双向队列长度 size = {size}')

    # 判断双向队列是否为空
    is_empty: bool = deque.is_empty()
    print(f'双向队列是否为空 = {is_empty}')