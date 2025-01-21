def is_empty():
    if len(stack) == 0:
        st: str = '是'
    else:
        st: str = '否'
    return st 

if __name__ == '__main__':

    # 初始化栈
    # Python中没有内置的栈类，可以把list当作栈来使用

    stack: list[int] = []

    # 元素入栈
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(f'栈 stack = {stack}')

    # 访问栈顶元素
    peek: int = stack[-1]
    print(f'栈顶元素 peek = {peek}')

    # 元素出栈
    pop: int = stack.pop()
    print(f'出栈元素 pop = {pop}')
    print(f'出栈后的 stack = {stack}')

    # 获取栈的长度
    size: int = len(stack)
    print(f'栈的长度 size = {size}')


    # 判断是否为空
    #is_empty: bool = len(stack) == 0
    a = is_empty()
    print(f'栈是否为空 = {a}')

    def is_empty():
        if len(stack) == 0:
            st: str = '是'
        else:
            st: str = '否'
        return st 