def g(l):
    a = 0
    for i in l:
        for j in i:
            if abs(i-j) > a:
                a = abds(i-j)
    return a
