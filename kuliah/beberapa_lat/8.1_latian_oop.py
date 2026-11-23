# NO 1
class Book:
    def __init__(self, title, pages):
        # TODO
        self.title = title
        self.pages = pages
        self.is_borrowed = False
        self.notes = []

    def setIsBorrowed(self, status):
        # TODO
        self.is_borrowed = status
        if status == True :
          print('Buku dipinjam.')
        else :
          print('Buku dikembalikan.')

    def addNote(self, note_text):
        # TODO
        self.notes.append(note_text)
        print(f"Catatan {note_text} ditambahkan.")

    def getDetails(self):
        # TODO
        status_teks = 'dipinjam' if self.is_borrowed else 'tersedia'
        return f"Buku {self.title} setebal {self.pages} halaman berstatus {status_teks} dengan catatan: {self.notes}"


book1 = Book("Laskar Pelangi", 529)
print(book1.getDetails())

book1.setIsBorrowed(True)
book1.addNote("bab 1 selesai")
book1.addNote("favorit")
print(book1.getDetails())

# >>> book1 = Book("Laskar Pelangi", 529)
# >>> print(book1.getDetails())
# Buku Laskar Pelangi setebal 529 halaman berstatus tersedia dengan catatan: []

# >>> book1.setIsBorrowed(True)
# Buku dipinjam.

# >>> book1.addNote("bab 1 selesai")
# Catatan bab 1 selesai ditambahkan.

# >>> book1.addNote("favorit")
# Catatan favorit ditambahkan.

# >>> print(book1.getDetails())
# Buku Laskar Pelangi setebal 529 halaman berstatus dipinjam dengan catatan: ['bab 1 selesai', 'favorit'] 

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('===============================================')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# NO 2

class Motorcycle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def speedUp(self):
        self.speed += 3

    def brake(self):
        self.speed -= 3


class FlyingVehicle:
    def __init__(self, brand, longitude, latitude, speed):
        self.brand = brand
        self.longi = longitude
        self.lat = latitude
        self.speed = speed

    def brake(self):
        self.speed -= 12

    def fly(self):
        print("Kendaraan sedang terbang")

# kode saya. 

class FlyingMotorcycle(FlyingVehicle, Motorcycle):
    def __init__(self, brand, longitude, latitude, speed):
        # TODO
        super().__init__(brand, longitude, latitude, speed)

    def speedUp(self):
        # TODO
        self.speed += 8

    def fly(self, longitude, latitude):
        # TODO
        super().fly()
        self.longi = longitude
        self.lat = latitude
        self.speed *= 3

m = FlyingMotorcycle(brand="Yamaha", longitude=1, latitude=1, speed=0)
m.speedUp()
m.speedUp()
print(m.speed)
m.fly(2, 3)
print(m.longi)
print(m.lat)
m.brake()
print(m.speed)
m.speedUp()
print(m.speed)

# contoh interaksinya

# >>> m = FlyingMotorcycle(brand="Yamaha", longitude=1, latitude=1, speed=0)
# >>> m.speedUp()   # speed += 8
# >>> m.speedUp()   # speed += 8
# >>> print(m.speed)
# 16
# >>> m.fly(2, 3)   # speed *= 3, longi = 2, lat = 3
# Kendaraan sedang terbang
# >>> print(m.longi)
# 2
# >>> print(m.lat)
# 3
# >>> m.brake()     # speed -= 12
# >>> print(m.speed)
# 36
# >>> m.speedUp()   # speed += 8
# >>> print(m.speed)
# 44


print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('===============================================')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# no 3

# jawab per line dari program soal ini 
import math

class Vector(object):
    def __init__(self, param1=1, param2=1, param3=1):
        self.x = param1
        self.y = param2
        self.z = param3

    def __len__(self):
        return int(math.sqrt(self*self))

    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == int:
            return Vector(other*self.x, other*self.y, other*self.z)
        else:
            return self

    def __str__(self):
        return f'<{self.x},{self.y},{self.z}>'

    def __rmul__(self, param):
        return self.__mul__(param)

v1 = Vector()
v2 = Vector(9,8,7)
result = v2*v1
print(v1)                       # Line 1 (1 poin)
print(result)                   # Line 2 (2 poin)
print(v2*3)                     # Line 3 (2 poin)
print(isinstance(7*v1,Vector))  # Line 4 (2 poin)
print(v2*'Fasilkom')            # Line 5 (2 poin)
print(len(Vector(1,2,2)))       # Line 6 (2 poin)

# soal no 4
# jawab per line dari program ini 

class FamilyMember:
    def __init__(self, name):
        self.__name = name
        self.__children = []

    def add_child(self, child):
        self.__children.append(child)

    def get_children(self):
        return self.__children

    def get_name(self):
        return self.__name

# ini soal nya perlu dilenkapi 
    # def __iter__(self):
    #     children_queue = []
    #     children_queue.______(#1)______          # 2 poin
    #     while ______(#2)______:                  # 1 poin
    #         current = ______(#3)______           # 2 poin
    #         del ______(#4)______                 # 2 poin
    #         children_queue.______(#5)______      # 2 poin
    #         ______(#6)______ ______(#7)______    # 1+1 poin
                
    def __iter__(self):
        children_queue = []
        children_queue.extend(self.__children)
        while len(children_queue) > 0:
            current = children_queue[0]
            del children_queue[0]
            children_queue.extend(current.get_children())
            yield current

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('===============================================')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# no 5

class Pecahan(object):
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    # belum selesai, akan dilanjutkan nanti

# Tahap no 1
print('>>>tahap 1<<<')
def gcd(x, y):
    '''Calculate the greatest common divisor of two positive integers'''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    '''Calculate the least common multiple of two positive integers'''
    return (x * y) // gcd(x, y)


class Pecahan(object):
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        # TODO
        return self.__str__()

    def __add__(self, param):
        # TODO
        the_lcm = lcm(self.denom, param.denom)
        numerator_sum = (the_lcm * self.numer // self.denom) + (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_sum, the_lcm)

    def __sub__(self, param):
        # TODO
        the_lcm = lcm(self.denom, param.denom)
        numerator_diff = (the_lcm * self.numer // self.denom) - (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_diff, the_lcm)

    def reduce(self):
        # TODO
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)

    def __eq__(self, param):
        # TODO
        reduce_self = self.reduce()
        reduce_param = param.reduce()
        return reduce_self.numer == reduce_param.numer and reduce_self.denom == reduce_param.denom

# trigger output

r1 = Pecahan(1, 2)
r2 = Pecahan(1, 3)
print(r1 + r2)
print(r1 - r2)
print(Pecahan(4, 2).reduce())
print(Pecahan(1, 2) == Pecahan(2, 4))
print(r1)

# >>> r1 = Pecahan(1,2)
# >>> r2 = Pecahan(1,3)
# >>> print(r1 + r2)
# 5/6
# >>> print(r1 - r2)
# 1/6
# >>> print(Pecahan(4,2).reduce())
# 2/1
# >>> Pecahan(1,2) == Pecahan(2,4)
# True
# >>> r1
# 1/2

# Tahap no 2
print('>>>tahap 2<<<')

def gcd(x, y):
    '''Calculate the greatest common divisor of two positive integers'''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    '''Calculate the least common multiple of two positive integers'''
    return (x * y) // gcd(x, y)

class Pecahan(object):
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        return self.__str__()

    def __add__(self, param):
        '''Add two pecahans'''
        if type(param) == int:
            param = Pecahan(param)
        the_lcm = lcm(self.denom, param.denom)
        numerator_sum = (the_lcm * self.numer // self.denom) + \
                        (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_sum, the_lcm)

    def __radd__(self, param):
        return self.__add__(param)

    def __sub__(self, param):
        '''Subtract two pecahans'''
        if type(param) == int:
            param = Pecahan(param)
        the_lcm = lcm(self.denom, param.denom)
        numerator_diff = (the_lcm * self.numer // self.denom) - \
                         (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_diff, the_lcm)

    def reduce(self):
        '''The reduced fractional value'''
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)

    def __eq__(self, param):
        '''Comparing two Pecahans for equality'''
        if type(param) == int:
            param = Pecahan(param)
        reduced_self = self.reduce()
        reduced_param = param.reduce()
        return reduced_self.numer == reduced_param.numer and \
        reduced_self.denom == reduced_param.denom

# trigger output

r = Pecahan(1, 2)
print(r + 1)
print(1 + r)
print(sum([Pecahan(1, 2), Pecahan(1, 3), Pecahan(1, 6)]))

# >>> r = Pecahan(1,2)
# >>> print(r + 1)
# 3/2
# >>> print(1 + r)
# 3/2
# >>> print(sum([Pecahan(1,2), Pecahan(1,3), Pecahan(1,6)]))
# 6/6

# Tahap no 3
print('>>>tahap 3<<<')

def gcd(x, y):
    '''Calculate the greatest common divisor of two positive integers'''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    '''Calculate the least common multiple of two positive integers'''
    return (x * y) // gcd(x, y)

class Pecahan(object):
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        return self.__str__()

    def __add__(self, param):
        '''Add two pecahans (Pecahan atau int)'''
        if type(param) == int:
            param = Pecahan(param)
        the_lcm = lcm(self.denom, param.denom)
        numerator_sum = (the_lcm * self.numer // self.denom) + \
                        (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_sum, the_lcm)

    def __radd__(self, param):
        return self.__add__(param)

    def __sub__(self, param):
        '''Subtract two pecahans'''
        if type(param) == int:
            param = Pecahan(param)
        the_lcm = lcm(self.denom, param.denom)
        numerator_diff = (the_lcm * self.numer // self.denom) - \
                         (the_lcm * param.numer // param.denom)
        return Pecahan(numerator_diff, the_lcm)

    def __mul__(self, param):
        '''Multiply two pecahans'''
        if type(param) == int:
            param = Pecahan(param)
        return Pecahan(self.numer * param.numer, self.denom * param.denom)

    def __rmul__(self, param):
        return self.__mul__(param)

    def reduce(self):
        '''The reduced fractional value'''
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)

    def __eq__(self, param):
        '''Comparing two Pecahans for equality'''
        if type(param) == int:
            param = Pecahan(param)
        reduced_self = self.reduce()
        reduced_param = param.reduce()
        return reduced_self.numer == reduced_param.numer and \
        reduced_self.denom == reduced_param.denom

# trigger output

r1 = Pecahan(1, 2)
r2 = Pecahan(1, 3)
print(r1 * r2)

# >>> r1 = Pecahan(1,2)
# >>> r2 = Pecahan(1,3)
# >>> r1 * r2
# 1/6