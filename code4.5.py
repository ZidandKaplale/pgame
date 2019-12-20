#PRAKTIKUM 4
#LATIHAN 4.5
#list(lanjutan dan hapus elemen list)

buah=["Durian","Mangga","Rambutan"]
print(buah)
print("Sebelum ditambah :", buah)
buah.append("Anggur")
print("Setelah ditambah :", buah)
buah.insert(0, "Pepaya")
print("Setelah ditambah :", buah)
buah.remove(buah[1])
print("Setelah dihapus [1] :", buah)
buah.remove("Anggur")
print("Setelah dihapus (Anggur) : ", buah)