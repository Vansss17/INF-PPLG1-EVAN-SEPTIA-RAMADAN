#for loop
for e in range (1,10):
    print("Juara ke-", e)
print("\n")

#while loop
print("Hitung mundur dimulai!!!")
hitungan = 10 
while (hitungan >= 1):
    print("hitugan ke- ", hitungan )
    hitungan -= 1 

print("Meluncur!!!")
print("\n")

#nested loop
for e in range(1,20): #loop ini berguna mengontrol jumlah baris yang keluar
    for s in range(1,20): #loop ini berguna mengontrol jumlah kolom di setiap baris
     print(e * s, end=' ') 
    print()