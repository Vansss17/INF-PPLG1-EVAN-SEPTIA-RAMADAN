#proses memasukan data ke dalam variabel
nama = "Evan"
#proses mencetak variabel
print(nama)

#nilai dan tipe data dalam variabel  dapat diubah
umur = 15                      #nilai awal
print(umur)                    #mencetak nilai umur
print(type(umur))              #mengecek tipe data umur
umur = "lima belas"            #nilai setelah diubah
print(umur)                    #mencetak nilai umur
print(type(umur))              #mengecek tipe data umur

namaDepan    = "Randy"
namaBelakang = "Ismail"
nama = namaDepan + " " + namaBelakang
umur = 30
hobi = "Membaca buku"
print("Biodata:\n", nama, "\n", umur, "\n", hobi)

#contoh variabel lainya
evansr   = "Halo,"
evan_s_r = "Hai,"
_evansr  = "Hi,"
evansr19170909 = "Bye,"

print("contoh variabel:\n", evansr , evan_s_r , _evansr , evansr19170909)

panjang = 100
lebar   = 50
luas    = panjang * lebar
print("panjang =", panjang ," ", "lebar =", lebar ," " )
print("panjang x lebar = ", luas )