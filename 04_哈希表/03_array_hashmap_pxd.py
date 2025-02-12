'''键值对类'''
class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

'''基于数组实现哈希表'''
class ArrayHashMap:
    # 构造方法
    def __init__(self):
        # 初始化数组，包含 100 个桶
        self.buckets: list[Pair | None] = [None] * 100

    # 哈希函数
    def hash_func(self, key: int) -> int:
        index = key % 100
        return index
    
    # 查询操作
    def get(self, key: int):
        index = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val
    
    # 添加操作
    def put(self, key: int, val: str):
        pair = Pair(key, val)
        index = self.hash_func(key)
        self.buckets[index] = pair
    
    # 删除操作
    def remove(self, key: int):
        index = self.hash_func(key)
        self.buckets[index] = None  # 置为 None，代表删除

    # 获取哈希表内所有键值对
    def entry_set(self) -> list[Pair]:
        result: list[Pair] =[]
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result
    
    # 获取所有键
    def key_set(self) -> list[int]:
        result: list[int] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result
    
    # 获取所有值
    def value_set(self) -> list[str]:
        result: list[str] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result
    
    # 打印哈希表
    def print(self):
        for pair in self.buckets:
            if pair is not None:
                print(f'{pair.key} -> {pair.val}')


'''测试代码'''
if __name__ == '__main__':
    # 初始化哈希表
    hmap = ArrayHashMap()
    
    # 添加操作，在哈希表中添加键值对（key, value)
    hmap.put(12347, '小哈')
    hmap.put(45753, '小啰')
    hmap.put(45825, '小算')
    hmap.put(12365, '小法')
    hmap.put(12345, '小鸭')
    print(f'\n添加完成后，哈希表为(key -> value):')
    hmap.print()

    # 查询操作
    name = hmap.get(12347)
    print(f'\n输入 12347 ，得到姓名 {name}')

    # 删除操作
    hmap.remove(45753)
    print(f'\n删除 45753 后，哈希表为(key -> value):')
    hmap.print()

    # 遍历哈希表
    print(f'\n遍历键值对 key -> value')
    for pair in hmap.entry_set():
        print(f'{pair.key} -> {pair.val}')
    
    print(f'\n单独遍历键 key')
    for key in hmap.key_set():
        print(f'{key}')
    
    print(f'\n单独遍历值 value')
    for value in hmap.value_set():
        print(value)
   