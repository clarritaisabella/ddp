from animal import Animal

class Amfibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas
    
    def info_amfibi(self):
        super().info_animal()
        print("jenis air \t\t\t : self.jenis_air",
              "\nbernapas \t\t\t : self.bernapas")

# Membuat objek dari kelas Amfibi
amfibi = Amfibi("katak", "serangga", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
amfibi.info_amfibi()