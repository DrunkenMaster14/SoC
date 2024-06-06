print(2)
index = 1
for number in range(3, 100000000, 2) : 
    check = 0
    for i in range(2, number) :
        if number%i == 0 :
            break
        if i == number - 1 :
            index += 1
            check = 1
    if index%100 == 1 and check == 1 :
            print(number)
