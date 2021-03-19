#2. Membuat program dictionary

dict1 ={'Nama':'Hasna Rifky','Hobi':'Membaca, mendengarkan musik, dan menulis',
       'Sosmed':'Instagram(@hasnarfky), Twitter(@hasnaaraa), dan WhatsApp(082137664738)',
       'Lagu':'Goodbye by Air Supply, My Love by Westlife, Hurt by Christina Aguilera',
       'Makanan':'Pempek, Soto, Pasta'}
print("Nama:",dict1['Nama'])
print("Hobi:", dict1['Hobi'])
print("Sosial media:", dict1['Sosmed'])
print("Lagu kesukaan:", dict1['Lagu'])
print("Makanan favorit:", dict1['Makanan'])
print(" ")

dict2 ={'Hobi1':'Membaca','Hobi2':'Mendengarkan musik','Hobi3':'Menulis'}
dict2['Hobi3'] = 'Menyanyi'

dict3 ={'Sosmed1':'Instagram(@hasnarfky)','Sosmed2':'Twitter(@hasnaaraa)','Sosmed3':'WA(082137664738)'}
dict3['Sosmed3'] = "Line(@hasnarifky.a)"

dict4 ={'Makanan1':'Pempek','Makanan2':'Soto','Makanan3':'Pasta'}
del dict4['Makanan2']
del dict4['Makanan1']

dict2['Hobi4'] = 'Jalan-jalan'

print("Hobi:",dict2['Hobi1'],",",dict2['Hobi2'],",",dict2['Hobi3'],", dan",dict2['Hobi4'])
print("Sosial media:",dict3['Sosmed1'],",",dict3['Sosmed2'],", dan",dict3['Sosmed3'])
print("Makanan favorit:", dict4['Makanan3'])
