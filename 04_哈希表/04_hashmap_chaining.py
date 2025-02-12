import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

'''键值对类'''
class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

'''链式地址'''
class HashMapChaining:
    # 构造方法，初始化
    def __init__(self):
        self.size = 0  # 键值对数量
        self.capacity = 4  # 桶数量
        self.load_thres = 2.0 / 3.0   # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

    # 哈希函数
    def hash_func(self, key: int) -> int:
        return key % self.capacity
    
    # 负载因子
    def load_factor(self) -> float:
        return self.size / self.capacity
    
    # 查询操作
    def get(self, key: int) -> str | None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若找到 key ，则返回对应 val
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None
    
    # 添加操作
    def put(self, key: int, val: str):
        # 当负载因子超过阈值时，执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，若遇到指定的 key， 则更新对应 val 并返回
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        # 若无该 key ，则将键值对添加至尾部
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1
    
    # 删除操作
    def remove(self, key: int):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶，从中删除键值对
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break
            elif pair.key == None:
                raise IndexError(f'不存在键为 {key} 的键值对')
            
    # 扩容哈希表
    def extend(self):
        # 暂存原哈希表
        buckets = self.buckets
        # 初始化扩容后的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 将键值对从原哈希表搬运至新哈希表
        for bucket in buckets:
            for pair in bucket:
                if pair.key != None:
                    self.put(pair.key, pair.val)
    
    # 打印哈希表
    def print(self):
        res = []
        for bucket in self.buckets:
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
        print(res)

'''Driver Code'''
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapChaining()

    # 添加操作，在哈希表中添加键值对（key, val)
    hashmap.put(12354, '小哈')
    hashmap.put(33456, '小啰')
    hashmap.put(98756, '小法')
    hashmap.put(334, '小算')
    print(f'\n添加完成后的哈希表为\nkey -> value')
    hashmap.print()
    
    # 查询操作，向哈希表输入键 key ，得到值 value
    name = hashmap.get(334)
    print(f'输入 key 334, 得到 value {name}')

    # 删除操作，在哈希表中删除键值对（key, val)
    hashmap.remove(12354)
    print(f'\n删除 key 12354 后，哈希表为： ')
    hashmap.print()

    



