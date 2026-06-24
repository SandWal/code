satuan = str(input("Apakah dalam C,R,F,K :"))#INPUT SATUAN DAN SUHUNYA BERAPA
temp = int(input("Berapa suhunya ?"))


if  satuan == "R":
    temp = round ( temp / 4) * 5
    print (f"Suhunya dalam Celcius adalah {temp} *C") #IF ELIF ELSE NYA BUAT NGUBAH DARI SUHU SELAIN CELCIUS
    #KE SUHU CELCIUS, CONTOH FARNHEIT KE CELCIUS DAN LAINNYA

elif satuan == "K":
    temp = round (temp -273)
    print (f"Suhunya dalam Celcius adalah {temp} *C")
elif satuan == "F":
    temp = round((temp-32 ) * 5/9)
    print (f"Suhunya dalam Celcius adalah {temp} *C")
elif satuan == "C":
    print (f"{temp}*C")
else :
    print ("MANA ADA!")

ubah = str(input("MAU UBAH KEMANA ? K,F,R :"))
if ubah == "K":
    temp = round(temp + 273)
    print (f"Suhunya dalam satuan Kelvin adalah {temp}*K") #INI PROSES LANJUTAN, BUAT NGUBAH CELCIUS KE SATUAN LAINNYA

elif ubah == "F":
    temp = round((temp * 9/5)+32)
    print (f"Suhunya dalam satuan Farenheit adalah {temp}*F")
elif ubah == "R":
    temp = round (temp /5)*4
    print(f"Suhunya dalam satuan Reamr adalah {temp}*R")

else :
    print("MANA ADA")

    

    



