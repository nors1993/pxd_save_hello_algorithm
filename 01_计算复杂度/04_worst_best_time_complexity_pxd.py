import random

def random_numbers(n: int) -> list[int]:
    '''生成随机数组'''
    # nums = [i for i in range(1, n + 1)]
    # random.shuffle(nums)
    nums = [random.randint(1, n) for _ in range(n)]  # 生成 n 个范围在 1 到 n之间的随机数(包括1和n)
    return nums

def find_one(nums: list[int]) -> int:
    '''查找数组 nums 中数字 1 所在索引'''
    for i in range(len(nums)):
        # 当元素 1 在数组头部时，达到最佳时间复杂度 O(1)
        # 当元素 1 在数组尾部时，达到最差时间复杂度 O(n)
        if nums[i] == 1:
            return i 
    return -1 # 未找到元素 1


if __name__ == "__main__":
    n = 10
    nums: list[int] = random_numbers(n)
    print(f"随机生成的数组🥷 :{nums}")
    index = find_one(nums)
    if index == -1:
        print("未找到元素 1")
    else:
        print(f"数字 1 的索引为🥷 :{index}")

