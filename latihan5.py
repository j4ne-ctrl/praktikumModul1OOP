#LATIHAN 5: ABSTRACTION & INTERFACE (MEMBUAT KONTRAK/STANDAR)
#Langkah kerja: Buat Blueprint Utama menggunakan modul abc

from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # Kita WAJIB membuat method serang, kalau tidak akan Error
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    # Implementasi serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
# unit = GameUnit() # ERROR! Abstract class tidak bisa jadi objek.
h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()


#================================================================================
#tugas analisis 5
#soal:
#1. Melanggar Kontrak: Hapus method serang di class Hero, lalu jalankan. Error apa yang muncul? Jelaskan arti error Can't instantiate abstract class Hero with abstract method...? Apa konsekuensinya jika lupa membuat method di Interface?
#2. Mencetak Cetakan: Coba aktifkan unit = GameUnit(). Mengapa class GameUnit dilarang dibuat jadi objek? Apa gunanya jika tidak bisa dibuat objek nyata?

#jawaban:
#1. Error yang muncul: TypeError: Can't instantiate abstract class Hero with abstract method serang.
#   Artinya, Hero dianggap masih bersifat abstrak dan tidak lengkap karena melanggar kontrak dengan tidak mengimplementasikan method serang(). Konsekuensinya, program akan menolak pembuatan objek (instansiasi) dari class Hero tersebut sampai semua method wajib dibuat.
#2. Class GameUnit dilarang jadi objek karena sifatnya masih berupa rancangan/konsep umum (abstrak) tanpa logika yang jelas. Gunanya dibuat hanya sebagai "blueprint/cetakan standar" agar semua class turunannya (seperti Hero dan Monster) memiliki struktur method yang seragam dan konsisten.
#================================================================================