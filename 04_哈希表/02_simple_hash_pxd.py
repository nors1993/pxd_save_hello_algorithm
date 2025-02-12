def add_hash(key: str) -> int:
    '''加法哈希'''
    hash = 0
    modulus = 1000000007  # 模数
    for c in key:
        hash += ord(c)  # ord()函数返回字符的ASCII码
    return hash % modulus

def mul_hash(key: str) -> int:
    '''乘法哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = 31 * hash + ord(c)
    return hash % modulus

def xor_hash(key: str) -> int:
    '''异或哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus

def rot_hash(key: str) -> int:
    '''旋转哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)  # 左移4位，右移28位，异或
    return hash & modulus

'''Driver code'''
if __name__ == '__main__':
    key = 'Hello 算法'

    hash_add = add_hash(key)
    hash_mul = mul_hash(key)
    hash_xor = xor_hash(key)
    hash_rot = rot_hash(key)
    print(f'加法哈希 hash_add = {hash_add}')
    print(f'乘法哈希 hash_mul = {hash_mul}')
    print(f'异或哈希 hash_xor = {hash_xor}')
    print(f'旋转哈希 hash_rot = {hash_rot}')



