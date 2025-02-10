import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_dict

# 初始化哈希表
hmap = dict[int, str]()

# 添加操作
# 在哈希表中添加键值对（key, value)

hmap[12345] = '小哈'
hmap[23478] = '小啰'
hmap[15737] = '小算'
hmap[31128] = '小法'
hmap[10583] = '小鸭'
print(f'添加完成后，哈希表为\nkey -> value')
print_dict(hmap)

# 查询操作
# 向哈希表中输入键 key ，得到值 value
name: str = hmap[31128]
print(f'\n输入学号 31128 ，查询到姓名 {name}')

# 删除操作
# 在哈希表中删除键值对（key, value)
hmap.pop(12345)
print(f'\n删除 12345 后，哈希表为\nkey -> value')
print_dict(hmap)

# 遍历哈希表
print(f'\n遍历键值对 key -> value')
for key, value in hmap.items():
    print(f'{key} -> {value}')

# 单独遍历 key
print(f'\n单独遍历 key')
for key in hmap.keys():
    print(key)

# 单独遍历 value
print(f'\n单独遍历 value')
for value in hmap.values():
    print(value)
