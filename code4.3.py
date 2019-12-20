#PRAKTIKUM
#LATIHAN 4.3
#STRING LANJUTAN

prodi = "Teknik Informatika"
konsen = "Jaringan"
mata_kuliah = "Pemrograman Game"
kampus = "UMMU"
lokasi = "Ternate"
tahun = 2019

print(prodi)
print(konsen)
print(mata_kuliah)
print(kampus)
print(lokasi)

print( '*' * 35 )
print("Prodi : ", prodi)
print("Konsentrasi : ", konsen)
print("Mata Kuliah : ", mata_kuliah)
print("Kampus : %s " % kampus)
print("Lokasi : %s " % lokasi)
print("Tahun : %d " % tahun)
print( '*' * 35 )
print("Prodi & Kampus : ", prodi, ",", kampus)
print("Prodi dan Kampus : ", prodi + ", " + kampus)
print("Prodi dan Kampus : %s, %s " % (prodi, kampus))