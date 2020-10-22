# номер 2
from abc import abstractmethod
class Clothes:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @abstractmethod
    def square(self):
        pass
    @property
    def full_square(self):
        return  self.width / 6.5 + 0.5+self.height*2+0.3





class Coat(Clothes):
    def square(self):
        cs=self.width / 6.5 + 0.5
        print(f'Расход ткани для пальто {cs}')
class Suit(Clothes):
    def square(self):
        ss=self.height*2+0.3
        print(f'Расход ткани для костюма {ss}')
s1=Suit(2,6 )
s1.square()
c1=Coat(2,7)
c1.square()
print(c1.full_square)



# номер 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __str__(self):
        return str(self.quantity * "*")

    def __add__(self, other):
        return Cell(int(self.quantity + other.quantity))
    def __sub__(self, other):
        if int(self.quantity-other.quantity)<0:
            print("Ошибка")
        else:
            return Cell(int(self.quantity-other.quantity))
    def __mul__(self, other):
        return Cell(int(self.quantity*other.quantity))
    def __truediv__(self, other):
        return Cell(int(round(self.quantity/other.quantity)))



cells1 = Cell(30)
cells2 = Cell(14)
print(cells1 + cells2)
print(cells1-cells2)
print(cells1*cells2)
print(cells1/cells2)


