'''========================================================
Graded Challange 1 

Nama : Adhy Arya Hendrata
Batch : BSD 00

membuat program shop cart dengan baik tanpa ada halangan
=========================================================
'''

Harga = []

class CartItem :
    
    def _init_(self,nama = str, harga=int):
        self.nama = nama
        self.harga = harga
        
    
class ShoppingCart :
    def _init_(self) : 
        self.Keranjang = []
        self.Total = []

    def add_Harga(self, harga):
        self.Total.append(harga)
        
    def add_Barang(self, barang):
        self.Keranjang.append(barang)

    def search_barang(self, search=str):
        
        hasil = []
        
        if len(self.Keranjang) < 1:
            print ('Keranjang lagi kosong')
        
        else : 
            for i in self.Keranjang:
                if search in i.nama.lower() or search in i.harga.lower():
                    result.append(i)
            
            return hasil
    def remove_barang (self, search=str):
        
        if len(self. Keranjang) < 1 : 
            print("Keranjang lagi Kosong")
            
        else : 
            for i in self.Keranjang:
                if search in i.nama.lower():
                    self.Keranjang.remove(i)
                    print (f'{search} dihapuskan dari Keranjang')
                else :
                    print ('barang tidak ditemukan')     
    
    def view_Keranjang(self):
        
        if len (self.Keranjang)< 1:
            print('Keranjang lagi Kosong')
            
        else : 
            print ("Barang di Keranjang: ")
            for i in range (len(self.Keranjang)):
                print(f'{i+1} {self.Keranjang[i].nama} {self.Keranjang[i].harga}')

             
    def total_belanja(self):      
        res = [eval(i) for i in self.Total]
        xtotal = 0
        for number in res:
          xtotal += number
          print (f"Total Belanja: Rp{xtotal:.2f}")          
   

def input_data (Item_keranjang=ShoppingCart):
    while True:
    
        print(''' 
Selamat Datang di Keranjang Belanja Toko Pasrah 

Menu : 
1. Menambah Barang 
2. Hapus Barang 
3. Tampilkan Barang di Keranjang
4. Lihat total Belanja
5. Exit''')
        
        menu = input('Tolong pilih nomor yang tersedia ')
        
        if menu == '1':
            nama_Barang = input("Barang apa yang mau ditambah ")
            harga_barang = input(("Masukkan harga Rp. "))
            taruh_barang = CartItem(nama_Barang,harga_barang)
            Item_keranjang.add_Barang(taruh_barang)
            Item_keranjang.add_Harga(harga_barang)
            #Harga.append(harga_barang)
            print(f'Barang {nama_Barang} berhasil ditambahkan')
            
        elif menu == '2':
            print ()
            print (' ---- Menghapus Barang ----')
            print ()
            find = input (' Barang yang dihapus :  ').lower()
            Item_keranjang.remove_barang(find)
            
        elif menu == '3':
            Item_keranjang.view_Keranjang()
        
        elif menu == '4':
            #print(f'Barang {Harga} berhasil ditambahkan')
            Item_keranjang.total_belanja()
            #res = [eval(i) for i in Harga]
            #total = 0
            #for number in res:
            #  total += number
            #print (f"Total Belanjas: Rp{total:.2f}")   
           

        elif menu =='5':
            print("Terima Kasih telah berbelanja!")
            break
        else :
            print ("Pilihan salah, tolong pilih nomor 1 ke 5.")
            
if _name_ == '_main_':
          katalog_belanja = ShoppingCart()
    
#run menu 
input_data(katalog_belanja)
