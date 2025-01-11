def constant(n: int) -> int:
    """常数阶"""
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count 

def linear(n:int) -> int:
    '''线性阶'''
    count = 0
    for _ in range(n):
        count += 1
    return count

def array_traversal(nums:list[int]) -> int:
    """线性阶（遍历数组）"""
    count = 0
    # 循环次数与数组长度成正比
    for num in nums:
        count += 1
    return count

def quadratic(n:int) -> int:
    '''平方阶'''
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count



if __name__ == '__main__':
    add = quadratic(8)
    print(f"add:{add}")  # python 3.6以上版本支持
    # add_a = linear(50)
    # add_b = linear(100)
    #print(f"add_a:{add_a}, add_b:{add_b}")  # python 3.6以上版本支持
    #print("add_a:{}, add_b:{}".format(add_a, add_b))


