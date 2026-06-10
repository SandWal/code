#Berat Badan
berat =float(input("Berapa Beratmu ?"))#input berat berupa angka desimal (float)
satuan =input ("Kilogram atau Pounds ? (K or L)") #menentukan satuan k atau L

if satuan == "K" :
    berat = berat * 2.205 #mengubah dari satuan K menjadi L
    satuan = "Lbs"
    print(f"Jadi beratmu adalah {round(berat,1)} {satuan}")
elif satuan == "L":
    berat = berat / 2.205#Mengubah dari satuan L menjadi K
    satuan = "Kg"
    print(f"Jadi beratmu adalah {round(berat,1)} {satuan}")
else :
    print(f"{satuan}bukan termasuk berat")


 #Mengeluarkan Hasil