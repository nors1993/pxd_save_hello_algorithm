class Mylist:
    '''列表类'''
    
    def __init__(self):
        '''构造方法'''
        self._capacity: int = 10  # 列表容量
        self._arr: list[int] = [0] * self._capacity  # 初始化数组
        self._size: int = 0  # 初始化列表长度（当前元素数量）
        self._extend_ratio: int = 2  # 每次列表扩容的倍数
    
    def size(self) -> int:
        '''获取列表长度（当前元素数量）'''
        return self._size
    
    def capacity(self):
        '''获取列表容量'''
        return self._capacity
    
    def get(self, index: int) -> int:
        '''访问元素'''
        # 如果索引越界，则抛出异常，下同
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
    
    def set(self, num: int, index: int):
        '''更新元素'''
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num: int):
        '''在尾部添加元素'''
        # 元素数量超出容量时，出发扩容机制
        if  self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] += num
        self._size += 1

    def insert(self, num: int, index: int):
        '''在中间插入元素'''
        if index < 0 or index >= self._size:
            raise IndexError('索引越界')
        # 元素数量超出容量时，触发扩容机制
        if self._size == self.capacity():
            self.extend_capacity()
        # 将索引 index 以及之后的元素都向后移一位
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        # 更新元素数量
        self._size += 1

    def remove(self, index: int) -> int:
        '''删除元素'''
        if index < 0 or index >= self._size:
            raise IndexError('索引越界')
        #num = self._arr[index]
        # 将索引 index 之后的元素都向前移动一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # 更新元素数量
        self._size -= 1
        # 返回被删除的元素
        #return num
    
    def to_arry(self) -> list[int]:
        '''返回有效长度的列表'''
        return self._arr[: self._size]

    def extend_capacity(self):
        '''列表扩容'''
        # 新建一个长度为原数组_extend_ratio倍的新数组，将原数组复制到新数组
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)

        # 更新列表容量
        self._capacity = len(self._arr)

'''Driver Code'''
if __name__ == '__main__':
    # 初始化列表
    nums = Mylist()
    # 在尾部添加元素
    nums.add(1)
    nums.add(2)
    nums.add(3)
    nums.add(4)
    nums.add(5)
    print(f'列表 nums = {nums.to_arry()}, 容量 = {nums.capacity()}, 长度 = {nums.size()}')

    # 在中间插入元素
    nums.insert(6, index=3)
    print(f'在索引 3 处插入数字 6 ，得到 nums = {nums.to_arry()}')

    # 删除元素
    nums.remove(3)
    print(f'删除索引为 3 处的元素， 得到 nums = {nums.to_arry()}')

    # 访问元素
    num = nums.get(1)
    print(f'访问索引 1 处的元素，得到 num = {num}')

    # 更新元素
    nums.set(0, 1)
    print(f'将索引 1 处的元素更新为 0， 得到 nums = {nums.to_arry()}')
    
    # 测试扩容机制
    for i in range(10):
        # 在 i = 5 时，列表长度将超过列表容量，此时出发扩容机制
        nums.add(i)
    print(f'扩容后的列表{nums.to_arry()}, 容量 = {nums.capacity()}, 长度 = {nums.size()}')
    

