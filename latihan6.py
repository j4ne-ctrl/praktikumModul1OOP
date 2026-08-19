#LATIHAN 6: POLYMORPHISM (FLEKSIBILITAS INTERAKSI)
#Langkah kerja: Gabungkan konsep Pewarisan Class Hero yang berbeda tipe

# Parent Class
class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")

# Child Class 1
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

# Child Class 2
class Archer(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

# Child Class 3
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


# -- Penerapan Polymorphism --
# Kita punya daftar hero campuran
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

print("--- PERANG DIMULAI ---")

# Satu perintah loop, tapi respon berbeda-beda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()


#================================================================================
#tugas analisis 6
#soal:
#1. Uji Skalabilitas: Buat class Healer(Hero) dengan method serang berisi print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!"). Masukkan objek Healer ke list pasukan. Apakah program berjalan lancar? Apa keuntungannya saat update game?
#2. Konsistensi Penamaan: Ubah nama method serang pada Archer menjadi tembak_panah. Apa yang terjadi? Mengapa nama method antara Parent dan Child Class harus persis sama dalam Polimorfisme?

#jawaban:
#1. Program berjalan LANJAR tanpa error sedikit pun. Keuntungannya, kode program sangat fleksibel (*scalable*). Programmer bisa menambah ratusan tipe hero baru tanpa perlu mengubah atau merusak logika utama (seperti perintah *looping*), sehingga pengembangan fitur game di masa depan jadi jauh lebih cepat dan aman.
#2. Yang terjadi adalah AttributeError atau Archer justru akan memanggil method serang() milik Parent (pilihan Hero tangan kosong), bukan aksi memanah. Penamaan method harus persis sama karena Polimorfisme mengandalkan *interface* yang seragam, di mana perintah pemanggilan tunggal (pahlawan.serang()) dapat langsung mengeksekusi method spesifik di tiap class anak secara otomatis.
#================================================================================