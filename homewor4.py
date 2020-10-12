# номер1
import sys
def salary(hours,rate):
    return int(hours)*int(rate)


params = sys.argv[1:]
if 'showsalary' in params:
    print('Ваша зарплата:',salary(sys.argv[2],sys.argv[3]))
elif 'help' in params:
    print('Програма для подсчёта вашей зарплаты:')
    print('Введите кодовую фразу "show salary"')
    print('Введите количество отработанных часов и ставку')


# номер2
lister=[1,13,45,67,8,9,0,45,3,4,67]
newlister=[]

for i in range(1,len(lister)):
    if lister[i]>lister[i-1]:
        newlister.append(lister[i])
print(newlister)



# номер 3
list17=[]
for i in range(20,240):
    list17.append(i)
newlist17=[x for x in list17 if x%20 ==0 or x%21 ==0]
print(newlist17)



# номер 4
from itertools import count
greatlist=[1,1,2,3,4,55,7,6,7,8,9,9,23,23,4,6]

newgreatlist=[x for x in greatlist if greatlist.count(x)==1 ]
print(newgreatlist)



# номер 5
from functools import reduce
uhulist=[]
for i in range(100,1000):
    uhulist.append(i)
print(uhulist)
newuhulist=[x for x in uhulist if x%2 == 0]
print(newuhulist)
def summmm(num1,num2):
    return num1+num2
print(reduce(summmm,newuhulist))



# номер 6
from itertools import count,cycle
import time
# 1
for i in count(4,):
    print(i)
    time.sleep(0.35)
    if i == 10:
        break
#2
c=0
days=['Понедельник', 'Среда' ,'Пятница']
for i in cycle(days):
    print(i)
    c += 1
    if c==25:
        break


# номер 7
from math import factorial
def generation(num):
    yield factorial(num)
print(list(generation(4)))