# ===================================================
# TUGAS PROYEK: SISTEM MANAJEMEN MYEDOTEL
# ===================================================

from abc import ABC, abstractmethod

# 1. ABSTRACTION & ENCAPSULATION (Parent Class)
class KamarHotel(ABC):
    def __init__(self, nama_kamar, stok, harga_dasar):
        self.nama_kamar = nama_kamar
        self.__stok = stok            # Private Attribute
        self.__harga_dasar = harga_dasar  # Private Attribute

    # Getter Stok
    def get_stok(self):
        return self.__stok

    # Getter Harga Dasar
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Method Ubah / Tambah Stok dengan Validasi
    def tambah_stok(self, jumlah):
        if jumlah < 0 or (self.__stok + jumlah) < 0:
            print(f"Gagal update stok {self.nama_kamar}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama_kamar}: {self.__stok} unit.")

    # Abstract Methods (Kontrak)
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass


# 2. INHERITANCE & POLYMORPHISM (Child Class 1)
class KamarDeluxe(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, fasilitas="Private Pool"):
        super().__init__(nama_kamar, stok, harga_dasar)
        self.fasilitas = fasilitas

    def hitung_harga_total(self, jumlah_malam):
        # Pajak sewa 10%
        pajak = 0.10 * self.get_harga_dasar()
        total_per_malam = self.get_harga_dasar() + pajak
        return total_per_malam * jumlah_malam

    def tampilkan_detail(self):
        pajak = 0.10 * self.get_harga_dasar()
        print(f"[DELUXE] {self.nama_kamar} | Fasilitas: {self.fasilitas}")
        print(f"Harga Dasar/Malam: Rp {self.get_harga_dasar():,.0f}".replace(",", "."))
        print(f"Pajak(10%): Rp {pajak:,.0f}".replace(",", "."))


# 3. INHERITANCE & POLYMORPHISM (Child Class 2)
class KamarStandard(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, kapasitas="2 Orang"):
        super().__init__(nama_kamar, stok, harga_dasar)
        self.kapasitas = kapasitas

    def hitung_harga_total(self, jumlah_malam):
        # Pajak sewa 5%
        pajak = 0.05 * self.get_harga_dasar()
        total_per_malam = self.get_harga_dasar() + pajak
        return total_per_malam * jumlah_malam

    def tampilkan_detail(self):
        pajak = 0.05 * self.get_harga_dasar()
        print(f"[STANDARD] {self.nama_kamar} | Kapasitas: {self.kapasitas}")
        print(f"Harga Dasar/Malam: Rp {self.get_harga_dasar():,.0f}".replace(",", "."))
        print(f"Pajak(5%): Rp {pajak:,.0f}".replace(",", "."))


# 4. FITUR PEMESANAN (Polymorphism di luar Class)
def proses_transaksi(daftar_pesanan):
    print("\n--- STRUK PEMESANAN ---")
    total_tagihan = 0
    no = 1
    
    for item in daftar_pesanan:
        kamar = item["kamar"]
        malam = item["malam"]
        
        subtotal = kamar.hitung_harga_total(malam)
        total_tagihan += subtotal
        
        print(f"{no}. ", end="")
        kamar.tampilkan_detail()
        print(f"Menginap: {malam} malam | Subtotal: Rp {subtotal:,.0f}".replace(",", "."))
        print()
        no += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}".replace(",", "."))
    print("----------------------------------------")


# ===================================================
# MAIN PROGRAM 
# ===================================================

print("--- SETUP DATA KAMAR ---")
# a) Admin membuat data kamar
deluxe1 = KamarDeluxe("Kamar Deluxe Sea View", 0, 1500000)
standard1 = KamarStandard("Kamar Standard Superior", 0, 500000)

# Uji Coba Stok
deluxe1.tambah_stok(10)
# b) Admin mencoba mengisi stok negatif (ditolak)
standard1.tambah_stok(-5)
# Mengisi stok valid
standard1.tambah_stok(20)

# c & d) Tamu memesan 2 malam Deluxe dan 1 malam Standard + Cetak Struk
pesanan_tamu = [
    {"kamar": deluxe1, "malam": 2},
    {"kamar": standard1, "malam": 1}
]

proses_transaksi(pesanan_tamu)