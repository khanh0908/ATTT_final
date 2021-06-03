from math import gcd as bltin_gcd
from random import randint

# tìm 1 phần tử sinh ngẫu nhiên
def findOnePrimitiveRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
    e = randint(1, modulo)
    while required_set != {pow(e, powers, modulo) for powers in range(1, modulo)}:
        e = randint(1, modulo)
    return e
#Tìm tất cả phần tử sinh
def primitiveRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                                                            for powers in range(1, modulo)}]


# gán giá trị số nguyên tố cần tìm phần tử nguyên thủy vào p
p = 19

print(primitiveRoots(p))
print(findOnePrimitiveRoots(p))