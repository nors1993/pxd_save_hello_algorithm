import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from modules import print_heap

'''大顶堆'''
class MaxHeap:
    # 构造方法，根据输入列表建堆
    def __init__(self, nums: list[int]):
        # 将列表元素原封不动添加进堆
        self.max_heap = nums
        # 堆化叶节点之外的其他其他所有节点
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    # 获取左子节点索引
    def left(self, i: int)-> int:
        return 2*i + 1
    
    # 获取右子节点索引
    def right(self, i: int) -> int:
        return 2 * i + 2
    
    # 获取父节点索引
    def parent(self, i: int):
        return (i - 1) // 2  # 向下整除
    
    # 交换元素
    def swap(self, i: int, j: int):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]
    
    # 获取堆大小
    def size(self) -> int:
        return len(self.max_heap)
    
    # 判断堆是否为空
    def is_empty(self) -> bool:
        return self.size() == 0
    
    # 访问堆顶元素
    def peek(self) -> int:
        return self.max_heap[0]
    
    # 元素入堆
    def push(self, val: int):
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size() - 1)
    
    # 从节点 i 开始，从从底至顶堆化
    def sift_up(self, i: int):
        while True:
            # 获取节点 i 的父节点
            p = self.parent(i)
            # 当越过根节点或节点无需修复时，结束堆化
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            # 否则交换两节点
            self.swap(i, p)
            # 循环向上堆化
            i = p
    
    # 从节点 i 开始， 从顶至底堆化
    def sift_down(self, i: int):
        while True:
            # 判断当前节点 i 、其左节点 l、其右节点 j 中的最大值，记为 ma
            l, ma, r = self.left(i), i, self.right(i)
            # 如果左节点存在（索引未越界）且左节点值大于当前节点值，最大节点为左节点 l
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            # 如果右节点存在（索引未越界）且右节点值大于当前节点值，最大节点为左节点 r
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            # 如果当前节点 i 最大或者索引 l, r 越界，则无需继续堆化，跳出循环
            if i == ma: 
                break
            # 交换两节点
            self.swap(i, ma)
            # 循环向下堆化 
            i = ma
    
    # 打印堆（二叉树）
    def print(self):
        print_heap(self.max_heap)

'''Driver Code'''
if __name__ == '__main__':
    # 初始化最大堆
    max_heap = MaxHeap([9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2])
    print(f'\n输入列表并建堆为')
    max_heap.print()

    # 获取堆顶元素
    peek = max_heap.peek()
    print(f'\n堆顶元素为 {peek}')

    # 元素入堆
    val = 10
    max_heap.push(val)
    print(f'\n元素 {val} 入堆后')
    max_heap.print()
    
    # 获取堆大小
    size = max_heap.size()
    print(f'\n堆元素数量为 {size}')

    # 判断堆是否为空
    is_empty: bool = max_heap.is_empty()
    print(f'\n堆是否为空 {is_empty}')




    
    

        
