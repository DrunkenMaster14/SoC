n = int(input('>'))
lst = []
for i in range(0, n) :
    ele = int(input('>'))
    lst.append(ele)

max_area = 0 
for i in range(0, n) :
    for j in range(i + 1, n + 1) :
        if min(lst[i : j])*(j-i) > max_area :
            max_area = min(lst[i : j])*(j-i)
            
print(max_area)