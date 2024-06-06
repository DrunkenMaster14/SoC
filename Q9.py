test_cases = int(input())
while test_cases > 0 :
    number = int(input())
    if number == 1 :
        print(1)
    else :
        count = 1 
        for i in range(2, number) :
            for j in range(2, i+1) :
                if i%j == 0 and number%j == 0 :
                    break
                if j == i :
                    count += 1
        print(count)
    test_cases -= 1