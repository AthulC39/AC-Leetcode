jar1= int(input(""))
jar2= int(input(""))
jar3= int(input(""))

largest = jar1

if jar2 > jar1:
    largest = jar2
    print(jar2 - jar1)
elif jar3 > jar1:
    largest = jar3
    print(jar3 - jar1)
else:
    print(jar1 - jar2)

