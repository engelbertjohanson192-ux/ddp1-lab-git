print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# SOAL NO 1
# class umumnya
class Employee : 
    def __init__(self,name, addres, phone_number, experience):
        self.name = name
        self.addres = addres
        self.phone_number = phone_number
        self.experience = experience

# kelas untuk programmer 
class programmer (Employee) :
    def __init__(self, name, addres, phone_number, experience, programming_language):
        super().__init__(name, addres, phone_number, experience)
        self.programming_language = programming_language

    def write_code (self) :
        return f"{self.name} sedang menulis kode menggunakan {self.programming_language}"

# kelas untuk manager 
class manager (Employee):
    def __init__(self, name, addres, phone_number, experience, team_size):
        super().__init__(name, addres, phone_number, experience)
        self.team_size = team_size

    def report_project_status (self):
        return f"{self.name} melaporkan status projek dari tim beranggotakan {self.team_size} orang"

    # 1. Membuat objek (instansiasi) dari kelas Programmer dan Manager
budi = programmer("Budi", "Depok", "08123456789", "3 Tahun", "Python")
siti = manager("Siti", "Jakarta", "08987654321", "7 Tahun", 10)

# 2. Mengeluarkan output metode khusus masing-masing kelas
print(budi.write_code())
print(siti.report_project_status())

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# SOAL NO 2
import math

class point :
    def __init__(self,x:int, y:int) :
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # methode untuk menghitung jarknya 
    def distance(self, other):
        dx = self.x - other.get_x()
        dy = self.y - other.get_y()
        return math.sqrt(dx**2 +dy**2)

    def __str__(self):
        return f"({self.x}, {self.y})"

titik_a = point (0,0)
titik_b = point (3,4)

print(f"Titik A berada di: x = {titik_a.get_x()}, y = {titik_a.get_y()}")
print(f"Titik B berada di: x = {titik_b.get_x()}, y = {titik_b.get_y()}")

# 3. Menghitung jarak antara titik_a dan titik_b
jarak = titik_a.distance(titik_b)
print(f"Jarak antara {titik_a} dan {titik_b} adalah: {jarak}")

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# SOAL NO 3
import math
class point_2 : 
    def __init__(self, x:int, y:int) :
        self.x = x
        self.y = y

    def get_x (self):
        return self.x

    def get_y (self):
        return self.y

    def distance (self, other) :
        dx = self.x - other.get_x()
        dy = self.y - other.get_y()
        return math.sqrt(dx**2 +dy**2)

    def __str__(self):
        return f"{self.x}, {self.y}"

# Kelas Anak (Child Class) yang mewarisi kelas Point
class labbelledPoints(point_2):
    def __init__(self, x:int, y:int, label:str):
        super().__init__(x, y)
        self.label=label

    def get_label(self):
        return self.label

    def __str__(self):
        return f"{self.label}{super().__str__()}"

# pemanggilan output

titik_p = labbelledPoints(0,0, "Titik Pusat")
titik_q = labbelledPoints(6,8, "TITIK Q")
print (f'Nama : {titik_q.get_label()}, kordinat : ({titik_q.get_x()}, {titik_q.get_y()})')

jarak = titik_p.distance(titik_q)
print (f'Jarak antara {titik_p} dan {titik_q} adalah : {jarak}')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
