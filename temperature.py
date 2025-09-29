unit = str(input("apakah dalam C/F:"))
temp = int(input("masukan suhu: "))

if unit == "C" :
    temp= round ((9 * temp) /5 + 32,1)
    print(f"suhunya dalam farenheit adalah {temp}*F")

elif unit =="F" :
    temp = round((temp -32)*5/9,1)
    print (f"suhu dalam celcius adalah {temp} *C")

else :
    print(f"{unit}tidak ada")