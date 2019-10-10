l=int(input('Число гони целое: '))
x=[1,2]
for i in range(2,l):
    for num in range(2,i):
        if not i%num:
            break
        elif num==(i-1):
            x.append(i)
print(x)
