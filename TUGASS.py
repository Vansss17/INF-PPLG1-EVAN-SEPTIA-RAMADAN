nilai1 = 100
nilai2 = 50 

print("===Kalkulator===")
print("1.Tambah")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
print("\n")

operator = int(input("Pilih operator : "))

if operator == 1:
    hasil = nilai1 + nilai2
    print("Hasil pertambahan : " , hasil)
elif operator == 2:
    hasil = nilai1 - nilai2
    print("Hasil pengurangan : " , hasil)
elif operator == 3:
    hasil = nilai1 * nilai2
    print("Hasil perkalian : " , hasil)
elif operator == 4:
    hasil = nilai1 / nilai2
    print("Hasil pembagian : " , hasil)


