import Crypto.Util.number
from Crypto.Util.number import bytes_to_long, long_to_bytes
from random import randint


# Crypto.Util.number.getPrime là hàm tạo số nguyên tố ngẫu nhiên với số bits theo yêu cầu
# Crypto.Util.number.inverse hàm tính nghịch đảo modunlo
# bytes_to_long chuyển đổi bytes thành số nguyên dài
# long_to_bytes ngược lại
##Hàm tính một phần tử sinh (phần tử nguyên thủy) bất kì với số p lớn
def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1
    while (1):
        g = randint(2, p - 1)
        if not (pow(g, (p - 1) // p1, p) == 1):
            if not pow(g, (p - 1) // p2, p) == 1:
                return g


bits = 256
print("Số bit yêu cầu của bài là:", bits)
# Khóa công khai (p, alpha, beta), khóa bí mật a
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
"""alpha là phần tử nguyên thủy theo mod  p . Code để tìm tất cả phần tử nguyên thủy với sô p nhỏ gửi ở file primitiveRoots.py đính kèm"""
alpha = find_primitive_root(p)
# Chọn số a
a = 5090
beta = pow(alpha, a, p)
print("\nKhóa công khai (p,alpha,beta)\n" + "p =", p, "\nalpha =", alpha, "\nbeta =", beta)
print("-----------------")
print("Khóa bí mật a\n" + "a =", a)
# Tìm số k thuộc Zp-1
k = randint(0, p - 2)

# Tiến hành mã hóa
msg = "Khanh-18020699"
print("\nBản tin là:", msg)
m = bytes_to_long(msg.encode('utf-8'))
y1 = pow(alpha, k, p)
y2 = (pow(beta, k, p) * (m % p)) % p
# Tiến hành giải mã
decipher = (y2 * Crypto.Util.number.inverse(pow(y1, a, p), p)) % p
m1 = long_to_bytes(decipher)
m1 = m1.decode('utf-8')
print("\nBản mã Elgamal:", "\ny1 =", y1, "\ny2 =", y2)
print("\nGiải mã Elgamal:", decipher, "tương đương bản tin:", m1)
