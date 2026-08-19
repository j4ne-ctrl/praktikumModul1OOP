import numpy as np
#LATIHAN 1: MEMBUAT CLASS HERO

class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name                 # Nama Hero
        self.hp = hp                     # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan

    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()


#================================================================================
#tugas analisis 1
#soal: Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = hero..? coba lakukan print(hero1.hp)

#jawaban: Nilai hp milik hero1 akan langsung berubah dari 100 menjadi 500
#================================================================================
