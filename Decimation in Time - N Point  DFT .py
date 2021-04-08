# -*- coding: utf-8 -*-
"""
Created on Tue APR 5 12:05:54 2021

@author: Dhruv Kanthaliya

USN : 1MS18EE015

DSP ASSIGNEMENT DIT-FFT
"""



import cmath


#taking input from the user
a=list(map(int,input("Enter the input for DFT : \n ").split()))



def transform(vector, inverse=False):
    n = len(vector)
    if n > 0 and n & (n - 1) == 0:  
        return transform_radix2(vector, inverse)
    else:  
        return transform_bluestein(vector, inverse)


#If the length of the passed input is a power of 2

def transform_radix2(vector, inverse):
    # Initialization
    n = len(vector)
    levels = _log2(n)
    exptable = [cmath.exp((2j if inverse else -2j) * cmath.pi * i / n) 
                for i in range(int(n / 2))]
    vector = [vector[_reverse(i, levels)] for i in range(n)]  # Copy with bit-reversed permutation
    
# Radix-2 decimation-in-time FFT
    size = 2
    while size <= n:
        halfsize = size / 2
        tablestep = n / size
        for i in range(0, n, size):
            k = 0
            for j in range(int(i), int(i + halfsize)):
                temp = vector[int(j + halfsize)] * exptable[int(k)]
                vector[int(j + halfsize)] = vector[j] - temp
                vector[j] += temp
                k += tablestep
        size *= 2
    return vector



#If input is other than power of 2


def transform_bluestein(vector, inverse):
    # Find a power-of-2 convolution length m such that m >= n * 2 + 1
    n = len(vector)
    m = 1
    while m < n * 2 + 1:
        m *= 2
    
    exptable = [cmath.exp((1j if inverse else -1j) * cmath.pi * (i * i % (n * 2)) / n) 
                for i in range(n)]  # Trigonometric table
    a = [x * y for (x, y) in zip(vector, exptable)] + [0] * (m - n)
    # Temporary vectors and preprocessing
    b = [(exptable[min(i, m - i)].conjugate() if (i < n or m - i < n) else 0) 
         for i in range(m)]
    c = convolve(a, b, False)[:n]  # Convolution
    for i in range(n):  # Postprocessing
        c[i] *= exptable[i]
    return c



def convolve(x, y, realoutput=True):
    assert len(x) == len(y)
    n = len(x)
    x = transform(x)
    y = transform(y)
    for i in range(n):
        x[i] *= y[i]
    x = transform(x, inverse=True)
    
# Scaling (because this FFT implementation omits it) and postprocessing
    
    if realoutput:
        for i in range(n):
            x[i] = x[i].real / n
    else:
        for i in range(n):
            x[i] /= n
    return x


# Returns the integer whose value is the reverse of the 
#lowest 'bits' bits of the integer 'x'.
def _reverse(x, bits):
    y = 0
    for i in range(bits):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y


# Returns the integer y such that 2^y == x, or raises 
#an exception if x is not a power of 2.
def _log2(x):
    i = 0
    while True:
        if 1 << i == x:
            return i
        elif 1 << i > x:
            raise ValueError("Not a power of 2")
        else:
            i += 1

#calling the function

b=transform(a)
print('\n The output is : \n')
for i in range(len(b)) :
    print(' '+'X'+'('+ str(i) + ')' + ' = ' + str(b[i]) + '\n' )
