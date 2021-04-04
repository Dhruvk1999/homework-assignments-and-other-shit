# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:32:44 2021

@author: Dhruv Kanthaliya

USN : 1MS18EE015

DIT-FFT DSP Assignment

"""

import cmath              # for complex numbers

#taking input from users

input=list(map(int,input(" Enter the input for 8 Point DFT \n ").split()))

#converting input to complex numbers

x0 = [complex(input[0],0),
      complex(input[1],0),
      complex(input[2],0),
      complex(input[3],0),
      complex(input[4],0),
      complex(input[5],0),
      complex(input[6],0),
      complex(input[7],0),]

#initializing 1st ,2nd and 3rd stage variables

x1 = [complex(0,0),
      complex(0,0),
      complex(0,0),
      complex(0,0),
      complex(0,0),
      complex(0,0),
      complex(0,0),
      complex(0,0),]

x2=x1.copy()
x3=x1.copy()

# Twiddle factor computation

w = cmath.exp(-complex(0, 1) * 2 * cmath.pi / 8)
w0 = w ** 0
w1 = w
w2 = w * w
w3 = w1 * w2

#computing output at diffrent stages

#stage 1

x1[0] = x0[0] + x0[4]
x1[1] = x0[0] - x0[4]

x1[2] = x0[2] + x0[6]
x1[3] = x0[2] - x0[6]

x1[4] = x0[1] + x0[5]
x1[5] = x0[1] - x0[5]

x1[6] = x0[3] + x0[7]
x1[7] = x0[3] - x0[7]

# Stage 2 

x2[0] = x1[0] + w0 * x1[2]
x2[1] = x1[1] + w2 * x1[3]
x2[2] = x1[0] - w0 * x1[2]
x2[3] = x1[1] - w2 * x1[3]

x2[4] = x1[4] + w0 * x1[6]
x2[5] = x1[5] + w2 * x1[7]
x2[6] = x1[4] - w0 * x1[6]
x2[7] = x1[5] - w2 * x1[7]

# Stage 3

x3[0] = x2[0] + w0 * x2[4]
x3[1] = x2[1] + w1 * x2[5]
x3[2] = x2[2] + w2 * x2[6]
x3[3] = x2[3] + w3 * x2[7]
x3[4] = x2[0] - w0 * x2[4]
x3[5] = x2[1] - w1 * x2[5]
x3[6] = x2[2] - w2 * x2[6]
x3[7] = x2[3] - w3 * x2[7]


#final output is stored in x3

# printing the final output

print('\n The output is : \n')
for i in range(8) :
    print('     '+'X'+'('+ str(i) + ')' + ' = ' + str(x3[i]) + '\n' )


# Thanks !


