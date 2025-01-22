class ArrayQueue:
    '''基于数组实现队列'''

    # 构造方法
    def __init__(self, size: int):
        self._nums: list[int] = [0] * size  # 初始化队列
        self._front = 0
        self._size = 0
    
    # 获取队列的容量（即队列最多能容纳多少个元素）
    def capacity(self) -> int:
        return len(self._nums)
    
    # 获取队列的长度（即队列元素个数）
    def size(self) -> int:
        return self._size
    
    # 判断队列是否为空
    def is_empty(self) -> bool:
        return self._size == 0
    
    # 入队
    def push(self, item: int):
        if self._size == self.capacity():
            raise IndexError('队列已满')
        # 计算队尾指针，指向队尾索引 + 1
        # 通过取余操作实现 rear 越过数组尾部后回到头部 —— 环形数组
        rear: int = (self._front + self._size) % self.capacity()
        self._nums[rear] = item  # 将item添加至队尾
        self._size += 1
    
    # 出队
    def pop(self) -> int:
        num: int = self.peek()
        # 指针向后移一位，若越过队尾，则返回数组头部 —— 环形数组
        self._front =  (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    # 访问队首元素
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('队列为空')
        peek = self._nums[self._front]
        return peek
        
    
    # 返回列表用于打印
    def to_list(self) -> list[int]:
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res

if __name__ == '__main__':
    # 初始化队列
    queue = ArrayQueue(10)

    # 元素入队
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(f'队列 queue = {queue.to_list()}')

    # 访问队首元素
    peek: int = queue.peek()
    print(f'队首元素 peek = {peek}')

    # 元素出队
    pop: int = queue.pop()
    print(f'出队元素 pop = {pop}')
    print(f'出队后 queue = {queue.to_list()}')

    # 获取队列长度
    size: int = queue.size()
    print(f'队列长度 size = {size}')

    # 判断队列是否为空
    is_empty: bool = queue.is_empty()
    print(f'队列是否为空 = {is_empty}')

    # def is_empty2(que: ArrayQueue):
    #     if que.is_empty():
    #         astr = '是'
    #     else:
    #         astr = '否'
    #     return astr
    # bstr = is_empty2(queue)
    # print(f'队列是否为空 = {bstr}') 

    # 测试环形数组
    for i in range(10):
        queue.push(i)
        queue.pop()
        print(f'第 {i + 1} 轮入队 + 出队后 queue = {queue.to_list()}')




