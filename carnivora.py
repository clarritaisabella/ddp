from animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit
    
    def info_carnivora(self):
        super().info_animal()
        print("Ukuran tubuh \t\t\t : ", self.ukuran_tubuh,
              "\nJenis kulit \t\t\t : ", self.jenis_kulit)

# Contoh penggunaan kelas Carnivora
harimau = Carnivora("Harimau", "Daging", "Darat", "Melahirkan", "Besar", "Bergaris")
harimau.info_carnivora()
print("=============")
serigala = Carnivora("Serigala", "Daging", "Darat", "Melahirkan", "Sedang", "Bulu")
serigala.info_carnivora()