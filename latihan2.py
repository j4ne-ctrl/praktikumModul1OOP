#LATIHAN 2: INTERAKSI ANTAR OBJEK
#Langkah kerja: tambahkan method serang dan diserang di dalam class hero

class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name                 # Nama Hero
        self.hp = hp                     # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan

    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang: Menerima damage
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method Info
hero1.info()
hero2.info()

# Output Pertarungan
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2) # Layla menyerang Zilong
hero2.serang(hero1) # Zilong membalas


#================================================================================
#tugas analisis 2
#soal: Perhatikan paramter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

#jawaban: sangat penting karena dengan mengoper objek utuh, method serang bisa langsung memanggil lawan.diserang() untuk mengubah dan mengurangi nilai hp lawan sefcara realtime
#================================================================================
