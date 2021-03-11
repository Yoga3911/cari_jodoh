import os, random, time
from alive_progress import alive_bar, config_handler
while True:
    os.system("cls")
    print("=== PROGRAM CARI JODOH ===")
    tanya1 = input("Nama anda: ")
    tanya2 = input("Nama orang yang disuka: ")
    cocok = random.randint(1, 100)
    print("Sedang menghitung kecocokan")
    config_handler.set_global(theme='ascii')
    with alive_bar(100, length=40) as bar:                                                                 
        for i in range(100):                                                                               
            time.sleep(.05)                                                                                
            bar()
    print("Tingkat kecocokan:", str(cocok)+"%")
    tanya3 = input("Apakah anda ingin mencoba kembali? [y/n] ")
    if tanya3 == "n":
        break