test_cases = int(input())
while test_cases > 0 :
    a = int(input())
    b = int(input())
    result = (a**b)%((10**9) + 7)
    print(result)
    test_cases -= 1
