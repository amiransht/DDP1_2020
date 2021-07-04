
#---------------------------------------------------------------------------------------------------------------
print("TUGAS PEMROGRAMAN 1")
#---------------------------------------------------------------------------------------------------------------

def main_menu():   
    print("Selamat datang di Program Konverter Bilangan")
    print("   1. Decimal ke Ternary")
    print("   2. Ternary ke Decimal")
    print("   3. Decimal ke Septenary")
    print("   4. Septenary ke Decimal")
    print("   5. Ternary ke Septenary")
    print("   6. Septenary ke Ternary")
    print("   7. Keluar")
    try: 
        operasi = int(input("Masukkan operasi yang ingin dilakukan: "))
        if type(operasi) == int:
            if operasi == 1:
                dec_to_basis("ternary")
            elif operasi == 2:
                basis_to_dec("ternary")
            elif operasi == 3:
                dec_to_basis("septenary")
            elif operasi == 4:
                basis_to_dec("septenary")
            elif operasi == 5:
                basis_to_basis("ternary","septenary")
            elif operasi == 6:
                basis_to_basis("septenary","ternary")
            elif operasi == 7:
                print("Terima kasih telah menggunakan program")
        else:
            raise ValueError
    except ValueError:
        print("Maaf input tidak valid")
        main_menu()

def dec_to_basis(nama_basis_tujuan):
    try:
        nilai_input = int(input("Masukkan input: angka: "))
        if type(nilai_input) == int: #Menjalankan operasi apabila input berupa integer
            basis_tujuan = []

            if nama_basis_tujuan == "ternary":
                basis = 3
            elif nama_basis_tujuan == "septenary":
                basis = 7
        
            #Mengubah desimal ke basis tujuan
            decimal = nilai_input
            while decimal > 0:
                basis_tujuan.append(decimal % basis)
                decimal = decimal // basis

            #Menampilkan hasil konversi
            print("Nilai",nama_basis_tujuan,"dari desimal",nilai_input,"adalah ",end="")
                
            for i in reversed(basis_tujuan):
                print(i, end="")
            main_menu()

        else:
            raise ValueError
    except ValueError:
        print("Input harus berupa angka desimal")
        main_menu()

def basis_to_dec(nama_basis_asal):
    try:
        nilai_input = int(input("Masukkan input: angka: "))

        if type(nilai_input) == int: #Menjalankan operasi apabila input berupa integer
            decimal = 0

            if nama_basis_asal == "ternary":
                basis = 3
            elif nama_basis_asal == "septenary":
                basis = 7

            #Mengubah basis asal ke decimal
            list_angka = []
            n = len(str(nilai_input))

            for i in str(nilai_input):
                list_angka.append(int(i))

            for i in list_angka:
                hasil = (i * (basis ** (n-1)))
                decimal += hasil
                n -= 1
        
            #Menampilkan hasil konversi
            print("Nilai desimal dari",nama_basis_asal,nilai_input,"adalah",decimal)
            main_menu()
    
        else:
            raise ValueError
    except ValueError:
        print("Input harus berupa angka", nama_basis_asal,"\b!")
        main_menu()

def basis_to_basis(nama_basis_asal, nama_basis_tujuan):
    try:
        nilai_input = int(input("Masukkan input: angka: "))

        if type(nilai_input) == int: #Menjalankan operasi apabila input bukan integer
            #Mengubah basis asal ke decimal
            decimal = 0

            if nama_basis_asal == "ternary":
                basis = 3
            elif nama_basis_asal == "septenary":
                basis = 7

            list_angka = []
            n = len(str(nilai_input))

            for i in str(nilai_input):
                list_angka.append(int(i))

            for i in list_angka:
                hasil = (i * (basis ** (n-1)))
                decimal += hasil
                n -= 1
                
            #Mengubah decimal ke basis tujuan
            basis_tujuan = []

            if nama_basis_tujuan == "ternary":
                basis = 3
            elif nama_basis_tujuan == "septenary":
                basis = 7

            while decimal > 0:
                basis_tujuan.append(decimal % basis)
                decimal = decimal // basis

            #Menampilkan hasil konversi
            print("Nilai",nama_basis_tujuan,"dari",nama_basis_asal,nilai_input,"adalah ",end="")
                
            for i in reversed(basis_tujuan):
                print(i, end="")
            main_menu()
        else:
            raise ValueError   
    except ValueError:
        print("Input harus berupa angka", nama_basis_asal, "\b!")
        main_menu()   

main_menu()

            






   

                       


