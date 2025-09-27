import time

my_time= int(input("masukan waktu lama tidur :"))

for x in range (my_time,0,-1) :
   
    second= x%60
    minute= int((x/60)%60)
    hours= int(x/3600)
    timer = (f"{hours:0=2}.{minute:0=2}.{second:0=2}")
    print(timer)
    time.sleep(1)
print("wake up")
    