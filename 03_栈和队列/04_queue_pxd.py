from collections import deque

'''
初始化队列
在 Python 中，我们一般将双向队列类 deque 看作队列使用
虽然 queue.Queue() 是纯正的队列类，但不太好用
'''
que: deque[int] = deque()

# 元素入队
que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)
print(f'队列 que = {que}')

# 访问队首元素
front: int = que[0]
print(f'队首元素 front = {front}')

# 元素出队
pop: int = que.popleft()
#pop: int = que.pop() # 双向队列删除队尾元素
print(f'出队元素为 pop = {pop}')
print(f'出队后的队列 que = {que}')

# 获取队列的长度
size: int = len(que)
print(f'队列长度 size = {size}')

# 判断队列是否为空
is_empty: bool = len(que) == 0
print(f'队列是否为空 = {is_empty}')