import random#import random dan string
import string
def generate_pasword(panjang): #mendefinisikan, jadi jika ada kode panjang, itu akan kembali keatas
    Kode = string.ascii_letters + string.digits + string.punctuation #mengumpulkan semua jenis


    pasword ="" #menyediakan tempat untuk pasword
    for i in range (panjang): #melooping pasword dari inputan tadi, dan ini diambil dari atas yang mendefinisikan panjang
        pasword += random.choice(Kode) #memilih acak/random
    return pasword #mengembalikan

panjang = int(input("Masukan Panjang passwordmu:")) #input panjang karakter
hasil = generate_pasword(panjang) #dikirim ke def generate_pasword
print (hasil)#menampilkan hasil
              
       