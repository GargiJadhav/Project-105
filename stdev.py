import pandas as pd
import math
x = [60,61,65,63,98,99,90,95,91,96]

n = len(x)

sum = 0

for i in x :
    sum = i+sum

mean = sum/n

print("Mean is " , mean)

squaredList=[]
for i in x :
    sub = i-mean
    sub = sub**2
    squaredList.append(sub)

sum = 0
for i in squaredList:
    sum = sum+i

divide = n-1

a = sum/divide

stdev = math.sqrt(a)

print("Standard Deviation using Algo is " , stdev)

#-------------------------------------------Statistics---------------------------------------------

import statistics as st

data = st.stdev(x)

print("Standard Deviation using Statistics is " , data)

# Yayy !! I got it , The stdev using statistics and algo is same :)