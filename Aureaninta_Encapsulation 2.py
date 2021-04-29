#Aureaninta TNKP (XI MIPA 5/06)

class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

aurea = Siswa(16002, "Aureaninta", "XI MIPA 5")

print(aurea.getnis())
aurea.setnis(16187)
print(aurea.getnis())
