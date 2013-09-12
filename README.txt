from math import exp


def simpsons(a, b, n):
    h = float(b-a)/n
    result = 0
    start = a
    slutt = b
    test = 0

    while(start<=slutt+h):
        if(start==a):
            result += function_value(start)
        elif(start==slutt):
            result += function_value(start)
        elif(test%2==0):
            result += 2*function_value(start)
        elif(test%2==1):
            result += 4*function_value(start)
        start = start + h
        test = test + 1
    return (h/3)*result

def function_value(v):
    return exp(-(v**2))

print(simpsons(-1, 1, 100))