## Objek SIswa
class Siswa:
    
    def __init__(self, nis, nama, alamat):
        self.nis = nis
        self.nama = nama
        self.alamat = alamat
        self.__mata_pelajaran = []
        self.__nilai = []
        
    def tampilkan(self):
        print("="*20)
        print(self.nis,self.nama,self.alamat)
        self.tampilkanNilai()
        self.tampilkanRataNilai()
        print("="*20)
    
    def tambahNilai(self, mapel, n):
        self.__mata_pelajaran.append(mapel)
        self.__nilai.append(n)
        
    def tampilkanNilai(self):
        for i,j in enumerate(self.__mata_pelajaran):
            print(i+1, self.__mata_pelajaran[i],self.__nilai[i])
    
    def tampilkanRataNilai(self):
        jumlah = 0
        for n in self.__nilai:
            jumlah += n
        rata = jumlah / len(self.__nilai)
        print("Rata-Rata Nilai",rata)
        
class SiswaSMK(Siswa):
    
    def __init__(self, nis, nama, alamat, jurusan):
        self.jurusan = jurusan
        super().__init__(nis, nama, alamat)
        
    def tampilkan(self):
        print("="*20)
        print(self.nis,self.nama,self.alamat)
        super().tampilkanNilai()
        super().tampilkanRataNilai()
        print("Jurusan : ", self.jurusan)
    
    
mikael = Siswa("12345", "Mikael", "Semarang")
yosua = SiswaSMK("12346", "Yosua", "Jakarta", "Rekayasa Perangkat Lunak")

## tambah nilai
mikael.tambahNilai("Matematika", 98)
mikael.tambahNilai("IPA", 95)
mikael.tambahNilai("Bahasa Inggris", 100)

mikael.tampilkan()

yosua.tambahNilai("Pemrograman Web", 100)
yosua.tambahNilai("Networking 1", 100)
yosua.tampilkan()

#mikael.tampilkanNilai()
#mikael.tampilkanRataNilai()
#yosua.tampilkan()