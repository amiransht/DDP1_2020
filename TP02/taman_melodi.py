import os, random


def generate_lagu(nama_file):
    with open(f"lagu/{nama_file}", 'r') as lagu_terpilih:
        lirik = lagu_terpilih.readlines()
    return lirik

def start_game():
    print("""
  _                                      
 | |__   ___ _ __ _ __   __ _  ___ _   _ 
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝ 
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗ 
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝                              
  """)
    print("~"*50)
    pemain = input("masukkan username     : ")
    mode = ''
    score = 0
    nyawa = 0
    ronde = 1
    lagu =  os.listdir("lagu")   

    while pemain == "null" or pemain == "":
        pemain = input("harap gunakan nama yang valid.\nmasukkan username     : ")
    while mode.lower() not in ["normal", "expert"]:
        mode = input("mode (normal/expert)  : ")    

    if mode.lower() == "normal":
        nyawa = 3
    else:
        nyawa = 1

    print("~"*50)
    print("Good Luck & Have Fun :)\n")

    #RONDE DIMULAI
    while ronde != 6 and not nyawa == 0:
        print(f"\nRound {ronde}")
        print(f"HP    : {nyawa}")
        print(f"Score : {score}")
        print("~"*50)
        
        #Memilih acak judul lagu
        judul_lagu = random.choice(lagu)
        lagu.remove(judul_lagu)
        print(f"Judul lagu: {judul_lagu}")
        
        #Memilih acak lirik misteri
        lirik = []
        for line in generate_lagu(judul_lagu):
            for i in [line.strip()]:
                lirik.append(i)
        
        while True:
            lirik_misteri = str(random.choice(lirik))
            if lirik_misteri not in lirik[0:4]:
                break
        index = lirik.index(lirik_misteri)

        #Menampilkan lirik prompt
        start = index - 4
        end = index
        for i in lirik[start:end]:
            print(i)

        #Menghitung panjang lirik prompt
        list_char = []
        for i in lirik[start:end]:
            for char in i:
                list_char.append(i)
        length = len(list_char)

        #User menjawab
        jawaban = input("Silakan menebak:\n")    
        if jawaban.casefold() == lirik_misteri.casefold():
            print("Jawaban BENAR")
            ronde += 1
            score += length     
        else:
            nyawa -= 1
            ronde += 1
            print("Jawaban SALAH")
            print("Jawaban :", lirik_misteri)
        
   
    if nyawa == 0:
        print("\nGAME OVER")
        print(f"Sayang sekali {pemain}, anda terhenti disini")
        print("Hasil akhir:")
        print(f"score   : {score}")
    else:
        print("\nSELAMAT!\nAnda berhasil menyelesaikan permainan")
        print("Hasil akhir:")
        print(f"score   : {score}")
    
    get_or_create_hs(mode, pemain, score)

    return pemain, mode, score, nyawa, lagu

        
def get_or_create_hs(mode, name, new_score):
    highscore = int(new_score)
    hs = os.listdir()
    #Mengecek jika file belum dibuat
    if "highscore.txt" not in hs: 
        text_file = open("highscore.txt", "w")
        a = "normal null 0\nexpert null 0\n"
        text_file.write(a)

    text_file = open("highscore.txt", "r")
    list_lines = text_file.readlines()
    data_normal = list_lines[0].split()
    data_expert = list_lines[1].split()
            
                   
    if mode == 'normal':
        prev_score = data_normal[2]
        if highscore  > int(prev_score):
            list_lines[0] = f"normal {name} {highscore}\n"
            text_file = open("highscore.txt", 'w')
            text_file.writelines(list_lines)

            print("NEW HIGH SCORE!!!")
            print(f"username : {name}")
            print(f"score    : {highscore}")
            print("Berhasil meraih highscore di mode normal")
        else:
            highscore = int(prev_score)
    elif mode == 'expert':
        prev_score = data_expert[2]
        if highscore > int(prev_score):
            list_lines[1] = f"expert {name} {highscore}\n"
            text_file = open("highscore.txt", 'w')
            text_file.writelines(list_lines)

            print("NEW HIGH SCORE!!!")
            print(f"username : {name}")
            print(f"score    : {highscore}")
            print("Berhasil meraih highscore di mode expert")
        else:
            highscore = int(prev_score)
    
    return highscore

start_game()
