import time
i = 0
x = 0
lst=[]

a = int(input("input first number"))
b = int(input("last number"))

for i in range (a,b+1):
    lst.append(i)

for i in range(a,b+1):
    for x in range(2,i):
        if i % x == 0:
            if lst.__contains__(i):
                lst.remove(i)

print(lst)
time.sleep(10)