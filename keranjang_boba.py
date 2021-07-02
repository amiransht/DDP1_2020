daftar_keranjang = []

def beli_keranjang(nama_keranjang, kapasitas_keranjang):
    daftar_keranjang.append([nama_keranjang] + [kapasitas_keranjang])
    print("Berhasil menambahkan", nama_keranjang, "dengan kapasitas", kapasitas_keranjang)

def jual_keranjang(indeks):
    daftar_keranjang.pop(indeks)
    print("Berhasil menjual", daftar_keranjang[indeks][0], "yang memiliki kapasitas sebesar", daftar_keranjang[indeks][1])
    
def ubah_kapasitas(indeks, kapasitas_baru):
    daftar_keranjang[indeks][1] = kapasitas_baru
    print("Berhasil mengubah kapasitas", daftar_keranjang[indeks][0], "menjadi", kapasitas_baru)

def ubah_nama(indeks, nama_baru):
    print("Berhasil mengubah nama", daftar_keranjang[indeks][0], "menjadi", nama_baru)
    daftar_keranjang[indeks][0] = nama_baru

def lihat(indeks):
    print("Keranjang", daftar_keranjang[indeks][0], "memiliki kapasitas sebesar", daftar_keranjang[indeks][1])

def lihat_semua():
    for i in range(0, len(daftar_keranjang)):
        print(daftar_keranjang[i][0], "          |", daftar_keranjang[i][1])

def total_kapasitas(list): 
    sum = 0
    for keranjang in list:
        sum += int(keranjang[1])
    return sum
    



#MAIN
jumlah_operasi = int(input("Masukkan banyak operasi: "))
for i in range(jumlah_operasi):
    operasi = input("Masukkan operasi: ")
    operasi = operasi.split()
    if operasi[0] == "BELI":
        beli_keranjang(operasi[1], operasi[2])
        pass
    elif operasi[0] == "JUAL":
        jual_keranjang(int(operasi[1]))
        pass
    elif operasi[0] == "UBAH_KAPASITAS":
        ubah_kapasitas(int(operasi[1]), int(operasi[2]))
        pass
    elif operasi[0] == "UBAH_NAMA":
        ubah_nama(int(operasi[1]), operasi[2])
        pass
    elif operasi[0] == "LIHAT":
        lihat(int(operasi[1]))
        pass
    elif operasi[0] == "LIHAT_SEMUA":
        print("Keranjang Dek Depe\n-----------------")
        lihat_semua()
        pass
    else:
        list = daftar_keranjang
        print("Total kapasitas keranjang Dek Depe adalah", total_kapasitas(list))
        pass
    
    
        
