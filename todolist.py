Jadwal =[]
Clock =[]

while True :
    List = input("Apa jadwal mu hari ini ?")
    if List == "q" :
        break
    else :
        When = input("Jam berapa ?")

        Jadwal.append(List)
        Clock.append(When)

        print (f" {Jadwal} : {Clock}")


        
