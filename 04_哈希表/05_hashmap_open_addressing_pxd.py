
'''键值对类'''
class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

'''开放地址寻址哈希表'''
class HashMapOpenAddressing:
    # 构造方法
    def __init__(self):
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 出发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets: list[Pair | None] = [None] * self.capacity  # 桶数组
        #self.buckets = [[] for _ in range(self.capacity)]
        self.TOMBSTONE = Pair(-1, '-1')  # 删除标记

    # 哈希函数
    def hash_func(self, key: int) -> int:
        return key % self.capacity
    
    # 负载因子
    def load_factor(self) -> float:
        return self.size / self.capacity
    
    # 搜索 key 对应的桶索引
    def find_bucket(self, key: int) -> int:
        index = self.hash_func(key)
        #bucket = self.buckets[index]
        first_tomestone = -1
        # 线性探测， 当遇到空桶时跳出
        while self.buckets[index] is not None:
            # 若遇到 key ， 返回对应的同索引
            if self.buckets[index].key == key:
                # 若之前遇到了删除标记， 则将键值对移动至该索引处
                if first_tomestone != -1:
                    self.buckets[first_tomestone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tomestone  # 返回移动后的桶索引
                return index  # 返回当前桶索引
            
            # 记录遇到的首个删除标记
            if first_tomestone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tomestone = index
            # 计算桶索引，越过尾部则返回头部
            index = (index + 1) % self.capacity
        # 如果 key 不存在，则返回添加的索引
        return index if first_tomestone == -1 else first_tomestone

    # 查询操作
    def get(self, key: int) -> int:
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 如果找到键值对，则返回对应 val
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        # 如果键值对不存在，则返回 None
        return None
    
    # 添加操作
    def put(self, key: int, val: str):
        # 当负载因子超过阈值时， 执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        # 搜索 key 对应的桶索引
        index = self.find_bucket(key)
        # 如果找到键值对，则更新对应 val
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        # 若键值对不存在，则添加该键值对
        self.buckets[index] = Pair(key, val)
        self.size += 1

    # 删除操作
    def remove(self, key: int):
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1
    
    # 扩容操作
    def extend(self):
        # 暂存原始哈希表
        buckets_tmp = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [None] *self.capacity
        self.size = 0
        # 将键值对从原始哈希表迁移至新哈希表
        for pair in buckets_tmp:
            if pair not in [None,self.TOMBSTONE]:
                self.put(pair.key, pair.val)
    
    # 打印哈希表
    def print(self):
        for pair in self.buckets:
            if pair is None:
                print('None')
            elif pair is self.TOMBSTONE:
                print('TOMBSTONE')
            else:
                print(f'{pair.key} -> {pair.val}')

'''Driver Code'''
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapOpenAddressing()
    
    # 添加操作
    hashmap.put(12354, '小哈')
    hashmap.put(33456, '小啰')
    hashmap.put(98756, '小法')
    hashmap.put(334, '小算')
    print("\n添加完成后，哈希表为\nKey -> Value")
    hashmap.print()

    # 查询操作
    name = hashmap.get(334)
    print(f'\n添加后，通过键 334 查询到的 Value 为 {name}')

    # 删除操作
    hashmap.remove(334)
    print("\n删除键 334 后，哈希表为\nKey -> Value")
    hashmap.print()


        
