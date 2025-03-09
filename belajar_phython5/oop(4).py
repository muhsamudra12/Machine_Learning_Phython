class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setName(self, name):
        self.__name = name
        
    def setAddress(self, address):
        self.__address = address
    
    def __str__(self):
        return f"{self.__name}, {self.__address}"


class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []        
    
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
    
    def __str__(self):
        return f"Student: {self.getName()}, {self.getAddress()}"


class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__courses = []
        
    def addCourse(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            return True
        return False  # Tidak perlu `else`, karena return di atas sudah keluar dari fungsi
        
    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)  # Langsung remove tanpa cari index
            return True
        return False  # Tidak perlu `else`
        
    def printCourse(self):
        print(self.__courses)
        
    def __str__(self):
        return f"Teacher: {self.getName()}, {self.getAddress()}"


# Testing Teacher class
t1 = Teacher("Pak Budi", "Jakarta")
print(t1)

t1.addCourse("Matematika")
t1.addCourse("Fisika")

t1.printCourse()
if t1.removeCourse("Biologi"):
    print("Berhasil Dihapus")
else:
    print("Gagal Dihapus")
t1.printCourse()
