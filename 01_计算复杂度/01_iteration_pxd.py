def for_loop(n: int) -> int:
    '''for 循环'''
    res = 0
    # 循环求和 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        res += i
    return res

def while_loop(n: int) -> int:
    '''while 循环'''
    res = 0
    i = 1 
    # 循环求和 1, 2, ..., n-1, n
    while i <= n:
        res += i
        i += 1
    return res

def while_loop_ii(n: int) -> int:
    '''while 循环（两次更新）'''
    res = 0
    i = 1
    # 循环求和 1, 4, 10, ...
    while i <=n:
        res += i
        i += 1
        i *= 2
    return res

def nested_for_loop(n: int) -> str:
    '''双层 for 循环'''
    res = ""
    # 循环 i = 1, 2, ..., n-1, n
    for i in range(1, n + 1):
        # 循环 j = 1, 2, ..., n-1, n
        for j in range(1, n + 1):
            res += f"({i}, {j}) "
    return res



if __name__ == "__main__":
    n = 3
    res = for_loop(n)
    print(f"\nfor 循环的求和结果 res = {res}")
    res = while_loop(n)
    print(f"\nwhile 循环的求和结果 res = {res}")
    res = while_loop_ii(n)
    print(f"\nwhile 循环（两次更新）求和结果 res = {res}")
    res = nested_for_loop(n)
    print(f"\n双层 for 循环结果 res = {res}\n")