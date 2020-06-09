print('helo')

a = 10
print(a, "judulnya" , type(a), bool(a))

#command
#command banyak, pake 3 kutip
"""data = input("masukan data: ")
print(data)

dataB = int(input("angka :"))
print(dataB, type(dataB))"""

b = 3
c = a // b
print(c)

d = (a +a) // b % c
print(d)

komparasi = a == 4
print(komparasi)

f = 10
print(hex(id(f)))
komparasiIs = a is f
print(komparasiIs)

at = False
c = not at
print(c)

e = at or c
g = at and c
h = at ^ c
print(e)
print(g)
print(h)

print("\n",22*"=","\n")

"""input = float(input('angka :'))
print(input)

ifinputmorethan0 = (input > 0)and (input < 3)
print(ifinputmorethan0)"""

a = 2
b = 1
c = a|b
print(c , ' binarynya :' , format(c, '08b'))