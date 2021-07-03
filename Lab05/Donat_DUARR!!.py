total_donat = int(input("Masukkan Jumlah Donat DUAARRR!!!: "))
menu = {} # key = nama donat, value = harga donat
rasa = {} # key = rasa donat, value = list harga donat

#INPUT MENU DONAT
for i in range(total_donat):
    data = input(f"Data {i + 1}: ").split()
    menu[data[0]] = int(data[1]) 
    if data[2] not in rasa:
        rasa[data[2]] = [int(data[1])]
    else:
        rasa[data[2]] = rasa.get(data[2]) + [int(data[1])]
    
#FUNSI-FUNGSI
def get_key(val):
    for key, value in menu.items():
        if val == value:
            return key

terjual = set() #nama donat terjual
pendapatan = [] #total pendapatan
def beli_nama(nama):
    if nama not in menu:
        print("Tidak ada Donat DUAARRR!!! dengan nama", nama, ":(")
    else:
        print(nama, "terjual dengan harga", menu[nama])
        terjual.add(nama)
        pendapatan.append(int(menu[nama]))

def beli_rasa(nama_rasa):
    if nama_rasa not in rasa:
        print("Tidak ada Donat DUAARRR!!! dengan rasa", nama_rasa, ":(")
    else:
        harga_termahal = max(rasa[nama_rasa])
        print(get_key(harga_termahal), "terjual dengan harga", harga_termahal)
        terjual.add(get_key(harga_termahal))
        pendapatan.append(int(harga_termahal))

#INPUT ORDER
jumlah_pembeli = int(input("\nMasukkan Jumlah Pembeli: "))
for i in range(jumlah_pembeli):
    order = input(f"Pembeli {i + 1}: ").split()
    if order[0] == "BELI_NAMA":
        beli_nama(order[1])    
    elif order[0] == "BELI_RASA":
        beli_rasa(order[1])
        
#SUMMARY
terjual = list(terjual) #convert set of nama donat terjual to list 
print("\nDonat Terjual:", ", ".join(terjual))
print("Total Pendapatan:", sum(pendapatan))
