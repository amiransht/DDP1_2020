in_filename = input("Masukkan nama file input: ")

try:
    read_file = open(in_filename).readlines()

    length = []
    for i in read_file:
        list_line = list(i)
        length.append(len(list_line))

    if length == []:
        empty = "##########\nNULL"
        output = open(in_filename,"a")
        output.write(empty)
        output.close()
    else:
        min = min(length)
        max = max(length)
        range = max - min

        text = "##########\nMin: {} karakter\nMax: {} karakter\nRange: {} karakter".format(min,max,range)
        output = open(in_filename,"a")
        output.write(text)
        output.close()

except FileNotFoundError:
	print("File tidak ditemukan :(")

else: # Diisi statement yang dijalankan ketika program berjalan tanpa error
    print("Output berhasil ditulis pada {in_filename}")

input("Program selesai. Tekan enter untuk keluar...")
