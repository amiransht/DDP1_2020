def rekursi(a):
    #base case
    if len(a) == 0:
        return ""
    elif isinstance(a, str):
        return a + ' '

    
    #recursive case
    else:
        return rekursi(a[0]) + rekursi(a[1:])


while True:
    data = input()

    if data == '':
        break

    isi = ' '.join(set(rekursi(eval(data)).split())) #Set will remove duplicate collection
    
    if len(isi) == 0:
        print('kosong')
    else:
        print(isi)
