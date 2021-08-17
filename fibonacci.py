x = int(input("enter terms"))

if(x == 0):
    print("num should be greater than 0")
if(x == 1):
    print(1)
if(x >= 1):
    print(0)
    print(1)
    n1 = 0
    n2 = 1
    counter = 0
    while(counter < x):
        n3 = n1+n2
        n1=n2
        n2=n3
        counter += 1
        print(n3)