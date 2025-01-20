'''
数组和列表的区别：
列表 是一种灵活且功能丰富的数据结构，适合用于存储各种数据类型。
数组 提供更高的性能，适合存储和处理相同类型的数值数据。

'''
import random

def random_access(nums: list[int]) -> int:
    '''随机访问元素'''
    # 在区间 [0, len(nums)-1] 中随机抽取一个数字
    random_index = random.randint(0, len(nums) - 1)
    # 获取并返回随机元素
    random_num = nums[random_index]
    return random_num

# 请注意，Python 的 list 是动态数组，可以直接扩展
# 为了方便学习，本函数将 list 看作长度不可变的数组
def extend(nums: list[int], enlarge: int) -> list[int]:
    '''扩展数组长度'''
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[i]
    # 返回扩展后的新数组
    return res

def insert(nums: list[int], num: int, index: int):
    '''在数组的索引 index 处插入元素 num'''
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋给 index 处的元素
    nums[index] = num
    return nums

def remove(nums: list[int], index: int):
    '''删除索引 index 处的元素'''
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]
    return nums

def traverse(nums: list[int]):
    '''遍历数组'''
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]
    print(f"通过索引遍历数组 count = {count}")
    # 直接遍历数组元素
    count  = 0
    for num in nums:
        count += num
    print(f"直接遍历数组元素 count = {count}")
    # 同时遍历数据索引和元素
    count = 0
    for i, num in enumerate(nums):
    #     count += nums[i]
    # print(f"同时遍历数据索引和元素 count = {count}")
          count += num
    print(f"同时遍历数据索引和元素 count = {count}")

def find(nums: list[int], target: int) -> int:
    '''在数组中查找指定元素'''
    for i in range(len(nums)):
        if nums[i] == target:
            return i, nums[i]
    return -1




if __name__ == "__main__":
    # nums = random.sample(range(1, 10), 5)
    nums = [random.randint(1, 10) for _ in range(5)]

    random_num = random_access(nums)
    print(f"\n随机访问的元素 random_num = {random_num}\n")
    
    nums = [1, 2, 3, 4, 5]
    nums = extend(nums, 3)
    print(f"扩展后的数组 nums = {nums}\n")

    nums = insert(nums, 20, 3)
    print(f"插入元素后的数组 nums = {nums}\n")

    nums = remove(nums, 3)
    print(f"删除元素后的数组 nums = {nums}\n")

    traverse(nums)

    find_num = find(nums, 3)
    print(f"查找元素的索引和元素 find_index, find_num = {find_num}\n")

    


