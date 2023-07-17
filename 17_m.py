# считываем файл
f = open('data17_m.txt')

a = [int(i) for i in f.readlines()] # считываем строки и записываем числовое значение в список
dop = [i for i in a if abs(i)%100 == 13] # числа, которые оканчиваются на 13
m = (dop[len(dop)//2-1] + dop[len(dop)//2]) / 2 # медиана списка dop
res = [] # разница пар

for x, y in zip(a, a[1:]): # считываем пары
     r = abs(x-y) # разница пары
     if r < 100000:
          if ((m%x == 0 ) and (m%y != 0)) or ((m%x != 0 ) and (m%y == 0)):
               res.append(abs(x-y))

print(len(res), min(res))

# закрываем файл
f.close()
