class Student:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address
        
    def addCourseGrade(self, course, grade):
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses += 1
        
    def printGrades(self):
        for i in range(len(self.__courses)):
            print(self.__courses[i] + " : " + str(self.__grades[i]))
            
    def getAverageGrade(self):
        if len(self.__grades) == 0:
            return 0  # Menghindari pembagian dengan nol
        total = sum(self.__grades)
        return total / len(self.__grades)


# Input jumlah siswa dan mata pelajaran
n_siswa = int(input("Masukkan Jumlah Siswa = "))
n_course = int(input("Masukkan Jumlah Course = "))

siswa = []
for i in range(n_siswa):
    nama = input(f"Masukkan Nama Siswa {i+1} = ")
    alamat = input(f"Masukkan Alamat Siswa {i+1} = ")
    siswa.append(Student(nama, alamat))
    
    for j in range(n_course):
        mapel = input(f"Masukkan Nama Mapel Siswa {nama} = ")
        nilai = int(input(f"Masukkan Nilai Mapel Siswa {nama} = "))
        siswa[i].addCourseGrade(mapel, nilai)

# Menampilkan hasil
print("\nHasil")
for i in range(n_siswa):
    print("\nNama:", siswa[i].getName(), "| Alamat:", siswa[i].getAddress())
    siswa[i].printGrades()
    print("Rata-Rata:", siswa[i].getAverageGrade())
