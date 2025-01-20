# 初始化列表
nums: list[int] = [1, 2, 3, 4, 5]
print(f'\n列表 nums = {nums}')

# 访问元素
x: int = nums[1]
print(f'\n访问索引 1 处的元素，得到 x = {x}')

# 更新元素
nums[1] = 0
print(f'\n将索引 1 处的元素更新为 0 ，得到 nums = {nums}')

# 清空列表
nums.clear()
print(f'\n清空列表后 nums = {nums}')

# 在尾部添加元素
nums.append(11)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
print(f'添加元素后的 nums = {nums}')

# 在中间插入元素
nums.insert(3, 6)
print(f'在索引 3 处插入元素，得到 nums = {nums}')

# 删除元素
nums.pop(3)
print(f'删除索引 3 处的元素，得到nums = {nums}')

# 通过索引遍历列表
count = 0
for i in range(len(nums)):
    count += nums[i]
# 直接遍历列表元素
    print(f"遍历得到的 count1 = {count}")
for num in nums:
    count += num
    print(f"遍历得到的 count2 = {count}")

# 拼接两个列表
nums1 = [6, 7, 8, 9, 10]
nums += nums1
print(f'\n拼接后的列表 nums = {nums}')

# 排序列表
nums.sort()
print(f'排序后的 nums = {nums}')
