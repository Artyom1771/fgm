# номер 1
lister = []
while True:
    T = input('Введите данные')
    if T =='':
        break
    else:
        T=T+'\n'
        lister.append(T)
with open('data1.txt', 'w')as g:
    g.writelines(lister)

# номер 2
# Школа
# Хоккей
# Програмирование
with open('data.txt') as f:
    tree=f.read()
s = 0
w = 0
for i in tree.split( ):
    s += 1
    w += 1
    print(f'{w} строка: {len(i)} слов')

print(f'Всего строк: {s}')

# номер 3
# Alex 25000
# Ivan 15000
# Artem 124000
# Katya 14900
# Sonya 23000
# Nastya 31000
# Gleb 93000
# Semen 39000
# Artur 56000
# Ignat 18000

with open('personnel.txt')as t:
    rtx=t.readlines()
good_persons=[]
allpay = []
for person in rtx:
    params=person.split()
    payment=int(params[1])
    if payment < 20000:
        allpay.append(payment)
        good_persons.append(params[0])
    else:
        allpay.append(payment)
print(good_persons)
print(f'Средняя зарплата всех сотрудников: {sum(allpay)/len(allpay)}')

# номер 4

# One - 1
# Two - 2
# Three - 3
# Four - 4

with open('number.txt',encoding='utf-8')as nt:
    lines=nt.readlines()

with open ('newnumber.txt','w',encoding='utf-8') as g:
    for line in lines:
        if '1' in line:
            line=line.replace('One','Один')
        elif '2' in line:
            line=line.replace('Two','Два')
        elif '3' in line:
            line=line.replace('Three','Три')
        elif '4' in line:
            line=line.replace('Four','Четыре')
        g.write(line)


# номер 5


with open('sumex.txt', 'w') as v:
    nums=input('Введите целые числа через пробел')
    v.write(nums)

def summm():
    cucumber = []
    with open('sumex.txt') as d:
        best = d.read()
    for q in best.split():
        cucumber.append(int(q))
    print(sum(cucumber))
summm()


# номер 6

# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —


dictionary=dict()
with open('lessons.txt',encoding='utf-8')as ls:
    lines=ls.readlines()
    for line in lines:
        nl=line.split()
        subj=nl[0]
        suml=sum([int(x[:x.find('(')]) for x in nl[1:] if '(' in x])
        dictionary[subj[:-1]]=suml
print(dictionary)


# номер 7

# frm1 ooo 10000 500
# firm2 oao 125000 83000
# firm3 ooo 134000 142000


import json
pardict=dict()
avprof=[]
#f_list=[pardict,avdict]
with open('frms.txt')as fm:
    firms=fm.readlines()
    for firm in firms:
        name,form, revenue, costs =firm.split()
        profit=int(revenue)-int(costs)
        pardict[name]=profit
        if profit >0:
            avprof.append(profit)
average_profit=sum(avprof)/len(avprof)
newlist=[pardict,{'average_profit': average_profit}]
print(newlist)

with open('json_newlist','w') as jessy:
    json.dump(newlist,jessy)

with open('json_newlist') as jessy3:
    print(json.load(jessy3))

