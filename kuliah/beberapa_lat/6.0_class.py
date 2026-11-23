class Counter:
    def __init__(self):
        self.value = 0

    def count(self):
        self.value += 1

    def reset(self):
        self.value = 0


# --- Kode untuk menjalankan dan melihat output ---
tally = Counter()
print("Nilai awal:", tally.value)

tally.count()
tally.count()
tally.count()
print("Setelah 3x count:", tally.value)

tally.reset()
print("Setelah reset:", tally.value)


# soal ke 2 tentang kerucut
import math
class cone:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def get_volume (self):
        volume = (math.pi * (self.base**2) * self.height)/3
        return volume

cone1= cone(10,12)
cone1.get_volume()