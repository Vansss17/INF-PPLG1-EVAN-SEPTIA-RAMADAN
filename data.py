#tipe data Boolean
#Boolean untuk menyatakan benar = 1 atau salah = 0
print(True)

#tipe data String
#String berguna untuk menyatakan huruf , angka , dan lain-lain
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah')
print("1,!,2,@")

#tipe data Integer
#Integer untuk menyatakan bilangan bulat
print(-20)

#tipe data Float
#Float untuk menyatakan bilangan yang mempunyai koma 
print(3.14)

#tipe data Hexadecimal
#Hexadecimal untuk menyatakan
print("Bentuk hexadecimal dari 23 adalah " + hex(23))

print("nama saya : " + "bagus")

#tipe data Complex
#Complex untuk menyatakan pasangan angka real dan imajiner
print(5j)

#tipe data List
#List untuk menyatakan untaian data yang dapat menyimpan berbagai tipe data yang isinya dapat diubah-ubah 
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
#Tuple untuk menyatakan untaian data yang dapat menyimpan berbagai tipe data yang isinya tidak dapat diubah-ubah 
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
#Dictionary untuk menyatakan untaian data yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai (key & value)
print({"nama":"Mail", 'umur':25})

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Danta", 'umur':17} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary