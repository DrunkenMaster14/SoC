test_cases = int(input())
while test_cases > 0 :
    strip_len  = int(input())
    k = int(input())
    strip = input()
    ans = 0
    while 'b' in strip :
        pos = strip.find('b')
        replaced_string = strip[pos : pos + k]
        strip = strip.replace(replaced_string, 'w'*k, 1)
        ans += 1
    print(ans)
    print(strip)
    test_cases -= 1