begin = int(input("begin: "))

end = int(input("end: "))

print()

print("Усі числа діапазону за спаданням:")

for i in range(end, begin - 1, -1):

    print(i, end=" ")

print()