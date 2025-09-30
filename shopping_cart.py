foods =[]
prices= []
total = 0

while  True:
   food= input("masukan belanjaan mu(q to quit)")
   if food == "q" :
      break
   else :
        price= float(input("masukan harga belanjaanmu : {food} $"))
        foods.append(food)
        prices.append(price)

print("-----Total Belanjaanmu------")

for food in foods :
    print (food , end =" ")
    
for price in prices :
    total += price
print()
print(f"total harga belanjaanmu adalah: $ {total}")
