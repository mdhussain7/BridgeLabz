def primes(n):
    array = [i for i in range(2,n+1)]
    p = 2

    while p <= n:
        i = 2*p
        while i <= n:
            array[i-2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]


if __name__ == '__main__':
    print(primes(1000))
    print()
    a = primes(1000)
    print()
    print("Prime Numbers between 0 to 100:")
    T100 = a[:25]
    print(T100)
    print()
    print("Prime Numbers between 101 to 200:")
    T200 = a[25:46]
    print(T200)
    print()
    print("Prime Numbers between 201 to 300:")
    T300 = a[46:62]
    print(T300)
    print()
    print("Prime Numbers between 301 to 400:")
    T400 = a[62:78]
    print(T400)
    print()
    print("Prime Numbers between 401 to 500:")
    T500 = a[78:95]
    print(T500)
    print()
    print("Prime Numbers between 501 to 600:")
    T600 = a[95:109]
    print(T600)
    print()
    print("Prime Numbers between 601 to 700:")
    T700 = a[109:125]
    print(T700)
    print()
    print("Prime Numbers between 701 to 800:")
    T800 = a[125:139]
    print(T800)
    print()
    print("Prime Numbers between 801 to 900:")
    T900 = a[139:154]
    print(T900)
    print()
    print("Prime Numbers between 901 to 1000:")
    T1000 = a[154:168]
    print(T1000)
    print()
