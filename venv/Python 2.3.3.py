# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num % 1000 //100
# d = num //1000
# print("Цифра в позиции тысяч равна", d)
# print("Цифра в позиции сотен равна", c)
# print("Цифра в позиции десятков равна", b)
# print("Цифра в позиции единиц равна", a)


#
# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num % 1000 //100
# d = num //1000
# e = a+d
# f = c-b
# if e==f:
#     print("ДА")
# else:
#     print("НЕТ")

# a = int(input())
# b = int(input())
# c = int(input())
# if b-a==c-b:
#     print("YES")
# else:
#     print("NO")
#
#     x = min(...)
# a = int(input())
# b = int(input())
# c = int(input())
#
# sum = 0;
# if a > 0:
#     sum += a
# if b > 0:
#     sum += b
# if c > 0:
#     sum += c
# print(sum)
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(0, a) + max(0, b) + max(0, c))

# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')

# a=int(input())
# if 999<a<=9999 and ((a%4==0 and a%100!=0) or a//400==0):
#     print("YES")
# else:
#     print("NO")

# x, y = int(input()), int(input())
# z = str(input())
# if z=="+":
#     print(x+y)
# elif z=="-":
#     print(x-y)
# elif z=="*":
#     print(x*y)
# elif z=="/":
#     if y==0:
#         print("На ноль делить нельзя!")
#     else:
#         print(x/y)
# else:
#     print("Неверная операция")

# x,y= str(input()), str(input())
# if (x=="красный" and y=="синий") or (y=="красный" and x=="синий"):
#     print("фиолетовый")
# elif (x=="красный" and y=="желтый") or (y=="красный" and x=="желтый"):
#     print("оранжевый")
# elif (x=="синий" and y=="желтый") or (y=="синий" and x=="желтый"):
#     print("зеленый")
# else:
#     print("ошибка цвета")

#
# a=int(input())
# if a==0:
#     print("зеленый")
# elif 0<a<=10 or 18<a<=28:
#     if a%2==0:
#         print("черный")
#     else:
#         print("красный")
# elif 10<a<=18 or 28<a<=36:
#     if a%2==0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")

# a1, b1 =int(input()), int(input())
# # a2, b2 =int(input()), int(input())
# # if b1<a2 or b2< a1:
# #     print("пустое множество")
# # elif a2<a1<b1 and a2<b1<b2:
# #     print(a1, b1)
# # elif a1<a2<b1 and a1<b2<b1:
# #     print(a2, b2)
# # elif a1<a2<b1 and a2<b1<b2:
# #     print(a2, b1)
# # elif a2<a1<b2 and a1<b2<b1: ####
# #     print(a1, b2)
# # elif a1<a2 and b1==b2:
# #     print(a2, b2)
# # elif a2<a1 and b1==b2:
# #     print(a1, b1)
# # elif a1==a2 and b1<b2:
# #     print(a1, b1)
# # elif (a1==a2 and b2<b1) or (a1==a2 and b1==b2):
# #     print(a2, b2)
# # elif a2==b1:
# #     print(b1)
# # elif a1==b2:
# #     print(a1)
#
# x1, y1 =int(input()), int(input())
# x2, y2 =int(input()), int(input())
# if x2>x1 and y2>y1:
#     if x2-x1==y2-y1: #or x2-x1==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x2>x1 and y1>y2:
#     if x2-x1==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x1>x2 and y1>y2:
#     if x1-x2==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x1>x2 and y2-y1:
#     if x1-x2==y2-y1:
#         print("YES")
#     else:
#         print("NO")
#
# elif x1==y1 or y2==y2:
#     print("NO")


# x1, y1 =int(input()), int(input())
# x2, y2 =int(input()), int(input())
# if (x2==x1-1 and (y2==y1+2 or y2==y1-2)) or (x2==x1-2 and (y2==y1-1 or y2==y1+1)):
#     print("YES")
# elif (x2==x1+1 and (y2==y1+2 or y2==y1-2)) or (x2==x1+2 and (y2==y1+1 or y2==y1-1)):
#     print("YES")
# else:
#     print("NO")

# x1, y1 =int(input()), int(input())
# x2, y2 =int(input()), int(input())
# #ход ладьи
# if x1 == x2 or y1 == y2:
#     print('YES')
# # ход слона
# elif x2>x1 and y2>y1:
#     if x2-x1==y2-y1: #or x2-x1==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x2>x1 and y1>y2:
#     if x2-x1==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x1>x2 and y1>y2:
#     if x1-x2==y1-y2:
#         print("YES")
#     else:
#         print("NO")
# elif x1>x2 and y2-y1:
#     if x1-x2==y2-y1:
#         print("YES")
#     else:
#         print("NO")
#
# elif x1==y1 or y2==y2:
#     print("NO")

# x = a % 10
# y = (a % 100) // 10
# z = a // 100
# aver = (max(x, y, z) - min(x, y, z))
# if aver == y:
#     print("Число интересное")
# else:
#     print("Число неинтересное")
# a=int(input())


# a, b=int(input()), int(input())
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
#         print(i)
#
# largest = -1
# for i in range(2):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)
#
# largest = int(input())  # принимаем первое число за максимальное
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)


# a,b =int(input()), int(input())
# count=0
# for i in range(a, b):
#     if i**3%10==4 or i**3%10==9:
#         count += 1
# print(count)
#
# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)
#
# n=int(input())
# counter=0
# for i in range(n):
#     num = int(input())
#     counter += num
# print(counter)
#
#
# n= int(input())
# z=list()
# st=list()
# for i in range(1, n+1):
#     a=int(input())
#     z.append(a)
#     max1=max(z)
# print(max1)
# st=z.remove(max1)
# max2=max(z)
# print(max2)
#
# n = int(input())
# a = 0
# b = 0
# for i in range(n):
#     num = int(input())
#     if num > a:
#         b = a
#         a = num
#     elif b < num < a:
#         b = num
#
# print(a)
# print(b)

# counter=0
# for i in range(10):
#     num = int(input())
#     if num % 2 == 0:
#         counter+=1
# if counter%2==0:
#     print('YES')
# else:
#     print('NO')
#
# fib1 = fib2 = 1
# print(fib1, end=" ")
#
# n = int(input())
# for i in range(2,n):
#     fib1,fib2=fib2,fib1+fib2
#     print(fib2, end=" ")
#
# n = int(input())
# summ = 0
# while 5>=n>=0:
#     if n==5:
#         summ+=1
#     n= int(input())
# print(summ)
#
#
# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)
#
# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)
#
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа
#     print(last_digit)

# num = int(input())
# minn=9
# maxx=0
# while num !=0:
#     last = num % 10
#     if last>maxx :
#         maxx=last
#     if last < minn:
#         minn= last
#     num = num // 10
# print(f"Максимальная цифра равна {maxx}")
# print(f"Минимальная цифра равна {minn}")

#
# num = int(input())
# count = 0
# last = num % 10
# num = num // 10
#
# while num != 0:
#     last_dig = num % 10
#     if last_dig != last:
#         count += 1
#     num = num // 10
#
# if count == 0:
#     print("YES")
# else:
#     print("NO")

n = int(input())
flag = True
a = n % 10
while n != 0:
    last = n % 10
    if last > a:
        flag = False
    n = n // 10
if flag == True:
    print("YES")
else:
    print("NO")





























