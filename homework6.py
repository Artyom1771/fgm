# номер 1
from time import sleep


class TrafficLight:
    def __init__(self):
       self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            i = 0
            while i < 3:
                print(TrafficLight.__color[i])
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(5)
                elif i == 2:
                    sleep(3)
                i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

# номер 2.1

class Road():
    def __init__(self):
        self.__length=int(input('Введите длину асфальта в метрах'))
        self.__width=int(input('Введите ширину асфальта в метрах'))
    def rd(self):
        print('масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см : 25 кг')
        print('толщинa полотна: 5 см')
        print('Вам потребуется',self.__length*self.__width*5*25 / 1000, 'тонн асфальта')
road1 = Road()
road1.rd()

# номер 2.2

class Road():
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def rd(self):
        print('масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см : 25 кг')
        print('толщинa полотна: 5 см')
        print('Вам потребуется',self.__length*self.__width*5*25 / 1000, 'тонн  асфальта')
road1= Road(2,3)
road1.rd()

# номер 3


class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._income={'wage': wage,'bonus': bonus}
class Position(Worker):
    def get_total_income(self):
        print(self._income['wage']+self._income['bonus'])
    def get_full_name(self):
        print(self.name+' '+self.surname)
worker1=Position('Катя','Некрасова','Бухгалтер',75000,5000)
worker1.get_total_income()
worker1.get_full_name()


# номер 4

class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=bool
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self,direction):
        print('Машина повернула',direction.lower())
    def show_speed(self, speed):
        print('Ваша скорость', speed)
class TownCar(Car):
    def show_speed(self,speed):
        if speed > 60:
            print('Превышение скорости!''\n''Ваша скорость',speed)
        else:
            print('Ваша скорость',speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self,speed):
        if speed > 40:
            print('Превышение скорости!''\n''Ваша скорость',speed)
        else:
            print('Ваша скорость',speed)


class PoliceCar(Car):
    pass

car1=TownCar(78,'Red','Toyota',False)
car1.show_speed(78)

car2=SportCar(230,'White','Ferrari',False)
car2.turn('Налево')

car3=WorkCar(39,'White','Nissan',False)
car3.go()

car4=PoliceCar(64,'Black/White','Ford',True)
car4.stop()


# номер 5


class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')
class Pencil(Stationery):
    def draw(self):
        print('Карандаш пишет')
class Handle(Stationery):
    def draw(self):
        print('маркер пишет')
first=Stationery('Firstobj')
first.draw()
pen=Pen('Ручка')
pen.draw()
pencil=Pencil('Карандаш')
pencil.draw()
handle=Handle('Маркер')
handle.draw()






