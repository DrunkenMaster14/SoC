a = int(input('>'))
b = int(input('>'))

if a == 1 or b == 1 :
    print(0)

for numbers in range(2, min(a, b) + 1) :
    if a%numbers == 0 and b%numbers == 0 :
        print(-1)
        break 
    if numbers == min(a, b) :
        print((a-1)*(b-1))

