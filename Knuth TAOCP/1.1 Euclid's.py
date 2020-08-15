list = [(33, 87), (456, 123), (90, 150)]

for m,n in list:
    # m = 55
    # n = 22
    r=-1
    while r!=0:
        r = m%n
        if r!=0:
            m = n
            n = r

    print(n)
