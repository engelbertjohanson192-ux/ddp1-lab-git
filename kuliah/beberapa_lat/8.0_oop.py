class Pecahan(object):
    def __init__(self, numer, denom = 1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        return "Pecahan" + \
            "(" + str(self.numer) + "," + str(self.denom) + ")"

class Pecahan1(object):
    def __init__(self, numer, denom = 1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        return self.__str__()

# Uji coba class Pecahan (Slide 1)
p1 = Pecahan(1, 2)
print("--- Hasil class Pecahan ---")
print(repr(p1))       # Hasil >>> p1
print(p1)             # Hasil >>> print(p1)
print(repr(str(p1)))  # Hasil >>> str(p1)

# Uji coba class Pecahan1 (Slide 2)
p2 = Pecahan1(1, 2)
print("\n--- Hasil class Pecahan1 ---")
print(repr(p2))       # Hasil >>> p2
print(p2)             # Hasil >>> print(p2)
print(repr(str(p2)))  # Hasil >>> str(p2)