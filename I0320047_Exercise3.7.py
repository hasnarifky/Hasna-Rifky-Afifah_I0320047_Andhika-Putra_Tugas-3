#Contoh cara menghapus pada Dictionary Python

dict ={'Name':'Zara','Age':7,'Class':'First'}

del dict['Name'] #Menghapus entri dengan key 'Name'
dict.clear() #Menghapus semua entri di dict
del dict #Menghapus dictionary yang sudah ada

print("dict['Age']:", dict['Age'])
print("dict['School']:", dict['School'])
