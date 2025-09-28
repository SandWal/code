import random
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower =  UPPER.lower()
number ="1234567890"
symbol =  "()*&^%$#!@:;><?/=+"

gede ,kecil, nums,syms = True ,True, True, True

all = ""
if gede :
    all += UPPER

if kecil :
    all += lower

if nums :
    all += number
if syms :
    all += symbol

panjang = 19
baris = 5

for x in range (baris):
    password="".join(random.sample(all, panjang))

    print(password)