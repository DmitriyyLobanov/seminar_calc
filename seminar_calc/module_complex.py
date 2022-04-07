import math

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b



def comp_sum():
    return complex(x) + complex(y)

def comp_mult():
    return complex(x) * complex(y)

def comp_sub():
    return complex(x) - complex(y)

def comp_dif():
    return complex(x) / complex(y)

def do_it(char):
    if char == '+':
        return complex(x) + complex(y)
    elif char == '-':
        return complex(x) - complex(y)
    elif char == '*':
        return complex(x) * complex(y)
    elif char == '/':
        return complex(x) / complex(y)