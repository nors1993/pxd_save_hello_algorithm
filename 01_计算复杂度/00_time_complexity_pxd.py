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

def bubble_sort(nums:list[int]) -> int:
    '''平方阶（冒泡排序）'''
    count = 0
    # 外循环：未排序区间为[0, i]
    for i in range(len(nums) - 1, 0, -1):
        # 内循环：将未排序区间[0, i]中的最大元素交换至该区间的最右端
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                count += 3 # 元素交换包含3个单元操作
    return nums, count 

def exponential(n: int) -> int:
    '''指数阶（循环实现）'''
    count = 1
    base = 1
    #print(base)
    # 细胞每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
            #
        base *= 2
        #print(base) 
    return count 

def exp_recur(n : int) -> int:
    '''指数阶（递归实现）'''
    if n == 1:
        return 1
    return exp_recur(n-1) + exp_recur(n-1) + 1 

def logarithmic(n: int) -> int:
    '''对数阶'''
    count = 0 
    while n > 1:
        n = n / 2
        count += 1
    return count




if __name__ == '__main__':
    add = logarithmic(4) # 
    print(f"🥷 :{add}")  # python 3.6以上版本支持
    # add_a = linear(50)
    # add_b = linear(100)
    #print(f"add_a:{add_a}, add_b:{add_b}")  # python 3.6以上版本支持
    #print("add_a:{}, add_b:{}".format(add_a, add_b))


