a = int(input())
b = int(input())
c = int(input())

if c%a == 0 or c%b == 0 :
    print('YES')

else :
    i = 0
    check = 0
    while a*i < c :
        j = 1
        while b*j < c - (a*i) :
            if (c-(a*i))%(b*j) == 0 :
                print('YES')
                check = 1
                break
            j += 1
        if check == 1 :
            break 
        i += 1
    if check == 0 :
        print('NO')