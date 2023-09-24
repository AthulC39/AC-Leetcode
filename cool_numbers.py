
start = int(input(""))
end = int(input(""))
loop = 0

for j in range(1, 22):
    if (j ** 6) <= end and (j ** 6) >= start:
        loop += 1
    elif (j ** 6) >= end:
        print(loop)
        break



