class Coffe:
    def __init__(self, nama_pelanggan="", total_bayar=0, jumlah_pesanan=0):
        self.nama = nama_pelanggan
        self.total_bayar = total_bayar
        self.jumlah_pesanan = jumlah_pesanan
        self.keranjang = {} 
        self.menu = {
            "Americano" : 20000,
            "Matcha Latte" : 25000,
            "Capuccino" : 27000,
            "Cofffe Latte" : 25000,
            "Espresso" : 20000,
            "Matchiato" : 27000,
        }

    def pemesanan(self):
        self.nama = input("Masukkan nama anda : ")
        while True:
            print("\n=================== MENU KOPI ===================")
            for nama_kopi, harga_kopi in self.menu.items():
                print(f"- {nama_kopi:<15} : Rp {harga_kopi:,}")
            print("____________________________________________________")
            
            try:
                pilihan = input("Pilih menu kopi yang anda inginkan : ").title()
                
                if pilihan not in self.menu:
                    print("Maaf menu yang anda masukkan belum tersedia/salah!")
                    continue
                    
                self.jumlah_pesanan = int(input(f"Masukkan jumlah {pilihan} yang ingin dibeli : "))
                if self.jumlah_pesanan <= 0:
                    print("Jumlah pesanan Tidak Boleh Nol!")
                    continue

                if pilihan in self.keranjang:
                    self.keranjang[pilihan] += self.jumlah_pesanan
                else:
                    self.keranjang[pilihan] = self.jumlah_pesanan
                
                tambah_pilihan = input("Apakah ada tambahan (ya/tidak)? : ").lower()
                if tambah_pilihan == "tidak":
                    break
            except ValueError:
                print("Maaf, input jumlah pesanan harus berupa angka!")

    def struk_pemesanan(self):
        if not self.keranjang:
            print("Tidak ada pesanan yang diproses.")
            return
            
        self.total_bayar = 0
        print(f"\n------------------------- STRUK PEMBELIAN ATAS NAMA: {self.nama.upper()} -------------------------")
        for kopi, jumlah in self.keranjang.items():
            harga_satuan = self.menu[kopi]
            subtotal = harga_satuan * jumlah
            self.total_bayar += subtotal
            print(f"- {kopi:<15} x {jumlah:<3} = Rp {subtotal:,}")
        print("-----------------------------------------------------------------------------")
        print(f"TOTAL BAYARAN ANDA: Rp {self.total_bayar:,}")
        print("-----------------------------------------------------------------------------")

def main():
    kasir = Coffe()
    kasir.pemesanan()
    kasir.struk_pemesanan()

if __name__ == "__main__":
    main()
