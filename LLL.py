import time

#Hitung mundur lampu lalu lintas, dari sudut pandang jalan pertama
print("Jalan pertama lampu hijau, 15 detik sebelum berhenti")
time.sleep(2)
Merah = int(15)

for x in range (Merah , 0, -1):
    second = x % 60
    print(f"{second :02}")
    time.sleep(1)

print("LAMPU MERAH, Berhenti!")

time.sleep(2)
print("Jalan Kedua giliran lampu hijau, jalan pertama berhenti")
time.sleep(2)
print("lampu hijau akan dimulai dalam")
time.sleep(2)
Hijau = int(15)

for y in range (Hijau, 0, -1):
    second = y % 60
    print(f"{second:02}")
    time.sleep(1)

time.sleep(1)
print("Lampu kuning, HATI HATI!")

time.sleep(2)
print("Lampu hijau, go")

time.sleep(2)
print("Sekarang giliran jalan kedua lampu merah")


