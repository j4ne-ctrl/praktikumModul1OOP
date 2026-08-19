#LATIHAN 4: ENKAPSULASI (MENGAMANKAN DATA HP)
#Langkah kerja: ubah hp jadi private (__hp), buat getter dan setter dengan validasi

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat Private
        self.__hp = hp_awal

    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)

# hero1.__hp = 9999     # GAGAL (Tidak akan mengubah hp asli)
# print(hero1.__hp)     # ERROR (Tidak bisa dibaca langsung)

hero1.set_hp(-50)       # Coba set negatif
print(hero1.get_hp())   # Output: 0 (Karena dicegat oleh logika Setter)


#================================================================================
#tugas analisis 4
#soal:
#1. Percobaan Hacking: Coba tambahkan print(f"Mencoba akses paksa: {hero1._Hero__hp}") di luar class. Apakah nilai HP muncul atau Error? Jelaskan konsep Name Mangling dan mengapa tetap tidak boleh dilakukan!
#2. Uji Validasi: Hapus logika if dan elif di dalam set_hp, lalu lakukan hero1.set_hp(-100). Apa yang terjadi dan mengapa Setter penting?

#jawaban:
#1. Nilai HP TETAP MUNCUL (tidak error). Ini terjadi karena fitur Name Mangling di Python mengubah nama variabel __hp menjadi _Hero__hp di belakang layar. Akses ini tetap tidak boleh dilakukan karena melanggar aturan enkapsulasi, merusak keamanan data, dan berisiko menimbulkan bug saat dikembangkan.
#2. Nilai HP Hero akan langsung berubah menjadi -100 (HP negatif, tidak logis). Method Setter sangat penting sebagai "filter/validasi" agar data atribut tidak bisa diisi oleh nilai ilegal, bug, atau cheat.
#================================================================================