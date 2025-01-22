from collections import deque

# 初始化双向队列
deq: deque[int] = deque()

# 元素入队
deq.append(1)
deq.append(2)
deq.append(3)
deq.append(4)
deq.append(5)
print(f'双向队列 deque = {deq}')

# 访问元素
front: int = deq[0] 
rear: int = deq[-1]
print(f"队首元素 front = {front}, 队尾元素 rear = {rear}")

# 元素出队
pop_front: int = deq.popleft()
print(f'队首出队后 deque = {deq}')
pop_rear: int = deq.pop()
print(f'队尾出队后 deque = {deq}')
print(f'队首出队元素 pop_front = {pop_front}, 队尾出队元素 pop_rear = {pop_rear}')

# 获取双向队列的长度
size: int = len(deq)
print(f'双向队列长度 size = {size}')

# 判断双向队列是否为空
is_empty: bool = len(deq) == 0
print(f'双向队列是否为空 = {is_empty}')

# def is_empty2(_deq: deque):
#     if len(_deq):
#         astr = '否'
#     else:
#         astr = '是'
#     return astr
# bstr = is_empty2(deq)
# print(f"双向队列是否为空： {bstr}")