import random #input randomm agar kode bisa memilih acak

Pilihan = ("Batu", "Gunting", "Kertas") #memasukan variabel
Player =None #player belum memilih
Komputer = random.choice(Pilihan) #BOT memilih

while Player not in Pilihan : #kode agar tidak memasukan selain pilihan
    Player = input("Mana yang kamu pilih (Batu, Gunting, Kertas) :")#player baru memasukan pilihannya

print(f"Pemain : {Player}")#menampilkan pilihan player
print(f"BOT : {Komputer}")#menampilkan pilihan BOT

if Player == Komputer : #ini if, elif, else, biasa 
    print("Seri")

elif Player == "Gunting" and Komputer == "Kertas":
    print("Menang")

elif Player == "Batu" and Komputer == "Guting":
    print("Menang")

elif Player == "Kertas" and Komputer == "Batu":
    print("Menang")

else :
    print("Kalah")