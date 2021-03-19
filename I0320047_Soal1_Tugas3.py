#1. Membuat program list (kaidah pemrograman list)

#Mengisi list
list =['Nadiya','Nana','Nadya','Hani','Vika','Issa','Nurki','Vian','Aji','Rian']

print("List teman awal:", list)

#Menampilkan isi list index
print("List index 4:", list[4])
print("List index 6:", list[6])
print("List index 7:", list[7])

#Mengganti isi list
list[3] = "Dhea"
list[5] = "Mira"
list[9] = "Ivan"
print("List teman setelah diganti:", list)

#Menambah isi list
list.extend(['Rara', 'Iffa'])
print("list teman setelah ditambah:", list)
print(" ")

#Menampilkan isi list dengan perulangan
for teman in list:
    print(teman, "adalah teman saya")
print(" ")

#Menampilkan panjang list
print("Panjang list:", len(list))
