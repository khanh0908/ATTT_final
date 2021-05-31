import Crypto.Util.number
from math import gcd as bltin_gcd
from random import randint
from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys

bits = 512

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

print ("Số lượng bit ",bits)
# Số n có độ dài 512 bits mà N=q.p nên sẽ chọn q và p có độ dài 256 bits
# Khóa công khai (n,e) khóa bí mật d
bitsQP = int(bits/2)

p=Crypto.Util.number.getPrime(bitsQP, randfunc=Crypto.Random.get_random_bytes)
print ("\nSố nguyên tố ngẫu nhiên p 256 bits: ",p)

q=Crypto.Util.number.getPrime(bitsQP, randfunc=Crypto.Random.get_random_bytes)
print ("\nSố nguyên tố ngẫu nhiên q 256 bits: ",q)

n=p*q

print ("\nn=p*q=",n)

PHI=(p-1)*(q-1)

print ("\nPHI=(p-1)(q-1)=",PHI)

#Tính e ngẫu nhiên
e = randint(1, PHI)
while bltin_gcd(PHI, e) != 1:
	e = randint(1, PHI)

#e=65537
print ("\ne=",e)
# Tính d
d=Crypto.Util.number.inverse(e,PHI)
print ("d=",d)

#print ("\nSố lượng chữ số (p): ",len(str(p)))
#print ("Số lượng chữ số (n): ",len(str(n)))
print("\nKhóa công khai (n,e)\n"+"n =",n,"\ne =",e)
print("-----------------")
print("Khóa bí mật d\n"+"d =",d)

# Mã hóa,giải mã
msg="Khanh-18020699"
print("\nBản tin là:",msg)
m = bytes_to_long(msg.encode('utf-8'))
enc=pow(m,e,n)
dec = pow(enc,d,n)
m1 = long_to_bytes(dec)
m1 = m1.decode('utf-8')

print("\nBản mã RSA:", enc)
print("\nGiải mã RSA:",dec,"tương đương bản tin:",m1)


