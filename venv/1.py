num = int(input())
minn=0
maxx=0
while num !=0:
    last = num%10
    if last>maxx:
        maxx,last=last,maxx

        if minn>maxx:
            maxx, minn=minn, maxx
        num = num // 10
print(f"Максимальная цифра равна {maxx}")
print(f"Минимальная цифра равна {minn}")