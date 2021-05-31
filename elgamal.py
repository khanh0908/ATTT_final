import Crypto.Util.number
from Crypto.Util.number import bytes_to_long, long_to_bytes
from random import randint

bits = 256
print("Số bit yêu cầu của bài là:",bits)
# Khóa công khai (p, alpha, beta), khóa bí mật a
p=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
"""alpha là phần tử nguyên thủy theo mod  p nhưng với bài tập này số p quá lớn
máy tính của em k đáp ứng được việc tìm phần tử nguyên thủy nên em đã chọn một số 
bất kì làm phần tử nguyên thùy. Code để tìm phần tử nguyên thủy với các số nhỏ hơn
được gửi ở file primitiveRoots.py đính kèm"""
alpha = 2
#Chọn số a
a = 5090
beta = pow(alpha, a, p)
print("\nKhóa công khai (p,alpha,beta)\n"+"p =",p,"\nalpha =",alpha,"\nbeta =",beta)
print("-----------------")
print("Khóa bí mật a\n"+"a =",a)
#Tìm số k thuộc Zp-1
k = randint(0, p-2)

#Tiến hành mã hóa
msg="Khanh-18020699"
print("\nBản tin là:",msg)
m = bytes_to_long(msg.encode('utf-8'))
y1 = pow(alpha, k, p)
y2 = (pow(beta, k, p) * (m%p)) % p
#Tiến hành giải mã
decipher = (y2*Crypto.Util.number.inverse(pow(y1,a,p),p))%p
m1 = long_to_bytes(decipher)
m1 = m1.decode('utf-8')
print("\nBản mã Elgamal:","\ny1 =",y1,"\ny2 =",y2)
print("\nGiải mã Elgamal:",decipher,"tương đương bản tin:",m1)

