#---------------------------------------------------------------------------------------------------------
print("LAB06\n")
#---------------------------------------------------------------------------------------------------------

# Mengambil input jumlah dan daftar nama donat dari user
total_donat = int(input("Masukkan Jumlah Donat DUAARRR!!!: "))
menu = {} # key = nama donat, value = harga donat
rasa = {} # key = rasa donat, value = list harga donat


for i in range(total_donat): # Mengambil input nama donat sebanyak total_donat
    data = input(f"Data {i + 1}: ").split() # Mengubah nama donat ke dalam bentuk list
    menu[data[0]] = int(data[1]) # Menambah dict menu
    if data[2] not in rasa:
        rasa[data[2]] = [int(data[1])] # Menambah dict rasa
    else:
        rasa[data[2]] = rasa.get(data[2]) + [int(data[1])] 
    
#FUNSI-FUNGSI
def get_key(val): #Mereturn key dari sebuah value
    for key, value in menu.items():
        if val == value:
            return key

terjual = set() #nama donat yang berhasil terjual
pendapatan = [] #total harga donat yang berhasil terjual

def beli_nama(nama): # Menjalankan operasi beli berdasarkan nama
    if nama not in menu:
        print("Tidak ada Donat DUAARRR!!! dengan nama", nama, ":(")
    else:
        print(nama, "terjual dengan harga", menu[nama])
        terjual.add(nama) # Menambah data nama donat yang berhasil terjual
        pendapatan.append(int(menu[nama])) # Menambah data harga donat yang berhasil terjual

def beli_rasa(nama_rasa): # Menjalankan operasi beli berdasarkan rasa
    if nama_rasa not in rasa:
        print("Tidak ada Donat DUAARRR!!! dengan rasa", nama_rasa, ":(")
    else:
        harga_termahal = max(rasa[nama_rasa]) # Memilih donat dengan harga termahal jika ada lebih dari ! donat dengan rasa sama
        print(get_key(harga_termahal), "terjual dengan harga", harga_termahal)
        terjual.add(get_key(harga_termahal)) # Menambah data nama donat yang berhasil terjual
        pendapatan.append(int(harga_termahal)) #Menambah data harga donat yang berhasil terjual

#Mengambil input orderan dari user
jumlah_pembeli = int(input("\nMasukkan Jumlah Pembeli: "))
for i in range(jumlah_pembeli): #Mengulang input data orderan sebanyak jumlah pembeli
    order = input(f"Pembeli {i + 1}: ").split() #Mengubah data orderan kedalam bentuk list
    if order[0] == "BELI_NAMA":
        beli_nama(order[1])    
    elif order[0] == "BELI_RASA":
        beli_rasa(order[1])
        
#SUMMARY
terjual = list(terjual) #convert set of nama donat terjual to list 
print("\nDonat Terjual:", ", ".join(terjual))
print("Total Pendapatan:", sum(pendapatan))


#CHALLENGE - WEBINAR
peserta_gabungan = []


for webinar in range(0,3):
    jumlah = int(input(f"\nJumlah nama yang akan dicatat untuk Webinar {webinar + 1}: "))
    daftar_hadir = set()

    for i in range(jumlah):
        data = input(f"Masukkan nama {i + 1}: ")
        daftar_hadir.add(data)

    peserta_gabungan.extend(daftar_hadir)

dict = {}
for nama in set(peserta_gabungan):
    dict[nama] = peserta_gabungan.count(nama)


x = ", ".join([f"{key}({value})" for key, value in dict.items() if key != ""])
if x == "":
    print("\nPeserta yang datang ke Webinar Donat DUAARRR!!!:\nTidak Ada")
else:
    print("\nPeserta yang datang ke Webinar Donat DUAARRR!!!:\n", "\b", x)

x = ",".join([key for key, value in dict.items() if value == 3])
if x == "":
    print("Peserta yang datang ke seluruh Webinar Donat DUAARRR!!!:\nTidak Ada")
else:
    print("Peserta yang datang ke seluruh Webinar Donat DUAARRR!!!:\n", x)

