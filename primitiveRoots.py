from math import gcd as bltin_gcd
from random import randint
# tìm 1 phần tử sinh(phần tử nguyên thủy) ngẫu nhiên
def findOnePrimitiveRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
    e = randint(1, modulo)
    while required_set != {pow(e, powers, modulo) for powers in range(1, modulo)}:
        e = randint(1, modulo)
    return e
#Tìm tất cả tìm 1 phần tử sinh(phần tử nguyên thủy)
def primitiveRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                                                            for powers in range(1, modulo)}]
#Tìm 1 tìm 1 phần tử sinh(phần tử nguyên thủy) bất kì tuy tính được với số p lớn nhưng vẫn có xác suất ra kết quả chưa chính xác
def find_primitive_root( p ):
		if p == 2:
				return 1
		p1 = 2
		p2 = (p-1) // p1
		while( 1 ):
				g = randint( 2, p-1 )
				if not (pow( g, (p-1)//p1, p ) == 1):
						if not pow( g, (p-1)//p2, p ) == 1:
								return g
# gán giá trị số nguyên tố cần tìm phần tử nguyên thủy vào p
p = 59169018583258959826490846615237125330837807713332135522858277102244488113243
#print(primitiveRoots(p))
print(find_primitive_root(p))
#print(findOnePrimitiveRoots(p))
