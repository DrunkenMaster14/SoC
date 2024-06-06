test_cases = int(input())
while test_cases > 0 :
    ans = 0
    number = int(input())
    for i in range(1, number + 1) :
        if number%i == 0 :
            ans += 1
    print(ans)
    test_cases -= 1