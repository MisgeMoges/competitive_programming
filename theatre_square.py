n, m, a = map(int, input().split())

def theatreSquare(n, m, a):
    if n%a == 0:
     val1 = n//a
    else:
     val1 = n//a+1

    if m%a == 0:
     val2 = m//a 
    else:
     val2 = m//a + 1
     
    print(val1*val2)

theatreSquare(6,6,4)
