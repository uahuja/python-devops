import sys

# Taking input in the CLI
a = float(sys.argv[1])
b = float(sys.argv[2])
o = sys.argv[3]

def add(a, b):
    sum = a+b
    return sum

def sub(a, b):
    s = a-b
    return s

def mul(a, b):
    m = a*b
    return m

if (o == 'add'):
    print(add(a,b))

elif (o == 'sub'):
    print(sub(a,b))

elif (o == 'mul'):
    print(mul(a,b))

else :
    print("No proper Operator")