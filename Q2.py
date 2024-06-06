test_cases = int(input())
while test_cases > 0 :
    nails = int(input())
    ans = 0
    while nails > 0 :
        height = int(input())
        rope_len = int(input())
        if height > rope_len  :
            ans = ans + 1
        nails = nails-1
    print(ans)
    test_cases -= 1