import libnum
import Crypto.Util.number
from random import randint
#Crypto.Util.number.getPrime là hàm tạo số nguyên tố ngẫu nhiên với số bits theo yêu cầu
bits = 160
print("Số bit yêu cầu của bài là:",bits)
# Chọn p,a,b
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
# y^2 = x^3 + 50x + 90
a = 50
b = 90
print("\nThu được đường cong y^2 = x^3 +",a,"x +",b,"mod(",p,")")
#Tạo đường cong bằng hàm ecc.Curve
curve = libnum.ecc.Curve(a, b, p)

# Hiển thị 100 điểm đầu tiên
P100=curve.find_points_in_range(1,100)
print(P100)

#Tìm 2 điểm có hoành độ bằng nhau ngẫu nhiên
P = curve.find_points_rand(1)
P1 = list(P[0])
print("\nDanh sách 2 điểm bất kì co hoành độ bằng nhau:\n",P1)
#Chọn điểm P tùy ý (Ở bài này chọn điểm P là điểm thứ nhất trong 2 điểm vừa tìm được bên trên)
#Chọn s làm khóa riêng
print("\nBên A thiết lập khóa công khai (E,Fp,P,B) và khóa riêng s")
P = P1[0]
s = 9050
## B = sP
B = curve.power(P, s)
print("E: y^2 = x^3 +",a,"x +",b)
print("Fp với p =",p)
print("P =",P)
print("B =",B)
print("Khóa riêng s = ", s)
# Chọn bản tin như điểm M thuộc E, chọn ngẫu nhiên số nguyên k bí mật
print("\nBên B chọn bản tin như M thuộc đường cong E,chọn ngẫu nhiên số nguyên k bí mật")
M = P100[50]
k = 9030
print("Điểm M = ",M)

# Tiến hành mã hóa
M1 = curve.power(P, k) #M1=kP
M2 = curve.add(M, curve.power(B, k)) #M2=M+kB
print("Bên B gửi bản mã cho bên A: (",M1,",",M2,")")
## Tiến hành giải mã M2-sM1

MD1 = curve.power(M1, s)
# Tính điểm đối của điêm MD1
MD1_2 = (MD1[0], -MD1[1])
decipher = curve.add(M2, MD1_2)
print("\nBên A giải mã thu được điểm bằng điểm M ban đầu và bằng ",decipher)
if M == decipher:
    print("Giải mã thành công....!")


