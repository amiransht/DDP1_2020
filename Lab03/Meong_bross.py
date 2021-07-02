banyak_perintah = input("\nBanyak perintah: ")
banyak_perintah = int(banyak_perintah)
x = 0
y = 0

if banyak_perintah >= 0:
    for i in range(banyak_perintah):
        perintah = input("Masukkan perintah: ")
        if perintah == "U":
            y += 1
        elif perintah == "S":
            y -= 1
        elif perintah == "T":
            x += 1
        elif perintah == "B":
            x -= 1
        elif perintah == "HOME":
            break
    print("Karakter Meong Bross berada di koodinat ", (x,y))
else:
    print("input banyak perintah harus bilangan non-negatif")


#CHALLENGE

import itertools
banyak_perintah = input("\nBanyak perintah: ")
banyak_perintah = int(banyak_perintah)
x = 0
y = 0

cartesian_list = [(x,y)]



if banyak_perintah >= 0:
    for i in range(banyak_perintah):
        perintah = input("Masukkan perintah: ")
        
        if perintah == "U":
            y += 1
            cartesian_list.append((x,y))
        elif perintah == "S":
            y -= 1
            cartesian_list.append((x,y))
        elif perintah == "T":
            x += 1
            cartesian_list.append((x,y))
        elif perintah == "B":
            x -= 1
            cartesian_list.append((x,y))
        elif perintah == "HOME":
            break
           
    print('Jalur yang ditempuh meong bross adalah ', end="")
 
    for a in range(banyak_perintah + 1):
        separator = "\b-"
        if a == banyak_perintah:
            separator = ""
        print(cartesian_list[a], separator, end="")    
else:
    print("input banyak perintah harus bilangan non-negatif")

