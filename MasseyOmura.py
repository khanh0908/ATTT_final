import libnum
import Crypto.Util.number
from random import randint
#Crypto.Util.number.getPrime là hàm tạo số nguyên tố ngẫu nhiên với số bits theo yêu cầu
bits = 16
print("Số bit yêu cầu của bài là:", bits)
# Chọn p,a,b
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
a = 50
b = 90
print("\nThu được đường cong y^2 = x^3 +",a,"x +",b,"mod(",p,")")
#Tạo đường cong bằng hàm ecc.Curve
curve = libnum.ecc.Curve(a, b, p)

# Hiển thị các điểm có hoành độ nằm trong khoảng từ 1 đến 100
P100=curve.find_points_in_range(1,100)
print(P100)

N = 1
for x in range(p):
    for y in range(p):
        if (y*y - x*x*x - a*x -b) % p == 0:
            N = N + 1

print("Hai bên A và B thống nhất với nhau đường cong E trên trường Fp:","\nE: y^2 = x^3 +",a,"x +",b,"\nFp với p =",p)
#Bên A Chọn bản tin như điểm M thuộc đường cong E, mà số nguyên bí mật mA thỏa mãn gcd(mA,N) = 1
#N là số điểm của đường cong. Nhưng với số bits lớn việc tính tổng số điểm mất nhiều thời gian,phức tạp, phần cứng máy tính chưa đảm bảo
# ==> Để thuận tiện trong demo chọn p khoảng 16bit
#N = p
print("N = ",N)
# Bên A Tính M1=(mA)M rồi gửi cho bên B
M = P100[50]
mA = 5683 #Chọn mA là số nguyên tố
M1=curve.power(M,mA)
print("\nBên A Tính M1=(mA)M rồi gửi cho bên B: \nM =",M,"\nmA =",mA,"\nM1 =",M1)
# Bên B nhận M1 chọn mB thỏa mãn gcd(mB,N) = 1. Tính M2=(mB)M1 rồi gửi cho bên A
mB = 56843 #Chọn mB là số nguyên tố
M2=curve.power(M1,mB)
print("\nBên B nhận M1 chọn mB thỏa mãn gcd(mB,N) = 1. Tính M2=(mB)M1 rồi gửi cho bên A: \nM1 =",M1,"\nmB =",mB,"\nM2 =",M2)
# Bên A nhận M2 tính mA^-1 thuộc ZN. Tính M3=(mA^-1)M2 rồi gửi cho bên B
mA1 = libnum.invmod(mA,N) #Một cách khác để tính nghịch đảo modulo là dùng libnum.invmod()
M3=curve.power(M2,mA1)
print("\nBên A nhận M2 tính mA^-1 thuộc ZN. Tính M3=(mA^-1)M2 rồi gửi cho bên B: \nM2 =",M2,"\nmA^-1 =",mA1,"\nM3 =",M3)
# Bên B nhận M3 tính mB^-1 thuộc ZN. Tính M4=(mb^-1)M3 lúc này M4=M1
mB1 = libnum.invmod(mB,N)
M4=curve.power(M3,mB1)
print("\nBên B nhận M3 tính mB^-1 thuộc ZN. Tính M4=(mB^-1)M3 rồi gửi cho bên B: \nM3 =",M3,"\nmB^-1 =",mB1,"\nM4 =",M4,"\nĐiểm M ban đầu:",M)
if M == M4:
    print("Giải mã thành công....!")