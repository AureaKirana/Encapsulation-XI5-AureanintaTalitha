#Aureaninta TNKP (XI MIPA 5/06)

class Siswa:
 
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
 
    #decorator
    @property
    def nis(self):
        pass
 
    #getter
    @nis.getter
    def nis(self):
        return self.__nis
 
    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis
 
wawak = Siswa(16158, "Najwa Zahra Ramadhani", "XI MIPA 5")
 
print(wawak.nis)
wawak.nis = 16089
print(wawak.nis)
