test_cases = int(input())
while test_cases > 0 :
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b >= 10 or a + c >= 10 or b + c >= 10 :
        print('YES')
    else :
        print('NO')
    test_cases -= 1