# membuat sistem kasir coffeshop sederhana 

class Coffe:
    def __init__(self, nama_pelanggan="", total_bayar=0, jumlah_pesanan=0):
        self.nama = nama_pelanggan
        self.total_bayar = total_bayar
        self.jumlah_pesanan = jumlah_pesanan

    def pemesanan(self):
        menu = {
            "Americano" : 20000,
            "Matcha Latte" : 25000,
            "Capuccino" : 27000,
            "Cofffe Latte" : 25000,
            "Espresso" : 20000,
            "Matchiato" : 27000,
        } 
        keranjang = {}
        while True:
            print("                        MENU KOPI                  ")
            for nama_kopi, harga_kopi in menu.items():
                print(f"- Nama kopi: {nama_kopi}, dengan harga {harga_kopi}")
                print("____________________________________________________")
                break
            try:
                 self.nama = input("Masukkan nama anda : ")
                 pilihan = input("pilih menu kopi yang anda inginkan : ").title()
                if pilihan not in menu:
                    print("Maaf menu yang anda masukan belum tersedia/salah")
                    continue
                self.jumlah_pesanan = int(input(f"Masukkan jumlah {pilihan} yang ingin dibeli : "))
                if keranjang in pilihan:
                    keranjang[pilihan] += self.jumlah_pesanan
                else: 
                    keranjang[pilihan] = self.jumlah_pesanan 

                tambah_pilihan = input("Apakah ada tambahan(ya/tidak)? : ").lower()
                if tambah_pilihan == "tidak":
                    break
            except ValueError:
                print("Maaf input yang dimasukkan harus berupa angka!")

    def struk_pemesanan(self):
        self.total_bayar = 0
        print(f"\n-------------------------STRUK PEMBELIAN ATAS NAMA: {self.nama}---------------------------------")
        for kopi, jumlah in self.keranjang.items():
            harga_satuan = menu[kopi]
            subtotal = harga_satuan * jumlah 
            self.total_bayar += subtotal 
            print(f"- {kopi}, {jumlah} = Rp{subtotal}")
        print("-----------------------------------------------------------------------------")
        print(f"TOTAL BAYARAN ANDA: {self.total_bayar:,}")
        print("-----------------------------------------------------------------------------")

def main():
    kasir = Coffe()
    kasir.pemesanan()
    print()
    kasir.struk_pemesanan()

if __name__ == "__main__":
        main()
