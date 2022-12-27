a,b = map(int,input('Введите два числа через пробел: ').split())

if a>b:

    for i in range(b,a+1):

        if i%2 == 1:

            print(i)

else:

    pass

if a<b:

    for i in range(a,b+1):

        if i%2 == 1:

            print(i)

else:

    pass