truk = ["10000", "tr"]
mobil = ["8000", "mb"]#membuat data berupa list
motor = ["6000", "mt"]

def KasihDiskon (kendaraan): #membuat fungsi
    harga = float(kendaraan[0])#mengambil harga asli
    match kendaraan[1]: #mengambil index ke 1 atau jenis kendaraan
        case "tr":
            return harga - harga * 0.3 #menentukan harga, dari harga asli dikurangi diskonnya
        case "mb":
            return harga - harga *0.5
        case "mt":
            return harga - harga * 0.4
    

print (KasihDiskon (truk))
print (KasihDiskon (mobil))#memanggil
print (KasihDiskon (motor))



    