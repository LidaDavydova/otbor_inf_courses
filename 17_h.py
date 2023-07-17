# функция для нахождения простого числа
def pr(n):
     if n == 2:
          return 1 # возвращаем 1, если простое
     if n <= 1:
          return 0 # непростое
     for i in range(2, int(n**0.5)+1):
          if n%i == 0:
               return 0 # возвращаем 0, если есть делитель
     return 1 # возвращаем 1, если простое

# считываем файл
f = open('data17_h.txt')

a = [int(i) for i in f.readlines()] # считываем строки и записываем числовое значение в список
dop = [i for i in a if pr(i)] # простые числа
mn = min(dop) # мин простых чисел
sr = sum(a) / len(a)
res = [] # произведение пар

for x, y in zip(a, a[1:]): # считываем пары
     sort = sorted([x, y]) # сортируем числа в паре
     if sort[0] < sr and sort[1] > sr and x%mn == 0 and y%mn == 0: # проверяем на условия
          res.append(x*y)

print(max(res), len(res))

# закрываем файл
f.close()

