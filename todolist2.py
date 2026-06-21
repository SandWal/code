TODO= []

while True :

    Menu = input("\nKamu Hari ini ngapain ?"
    "\n1.Tambah jadwal"
    "\n2.Lihat Jadwal"
    "\n3.Hapus"
    "\n4.Keluar"
    "\n Masukkan Perintah :")
    if Menu == "1":
        Jadwal = input("Masukan Jadwal mu kawan :")
        TODO.append(Jadwal)
    elif Menu =="2":
        for item in TODO :
            print(item)
    elif Menu == "3":
        TODO.pop(input("...."))
    else :
        Menu == "4" 
        break
    
print("----Jadwal Ku Hari Ini----")
print(TODO)

    

