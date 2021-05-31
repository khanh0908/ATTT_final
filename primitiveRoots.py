from math import gcd as bltin_gcd


def primitiveRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo)}
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                                                            for powers in range(1, modulo)}]


# gán giá trị số nguyên tố cần tìm phần tử nguyên thủy vào p
p = 17
print(primitiveRoots(p))
