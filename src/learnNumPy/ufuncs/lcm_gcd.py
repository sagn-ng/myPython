import numpy as np
num1, num2=25, 10
print(np.lcm(num1, num2), np.gcd(num1, num2))

arr=np.array([10, 7, 25])
#to evaluate LCM or GCD in an array, use the reduce() method in the lcm() (or gcd()) func.
x=np.lcm.reduce(arr)    #x=350
y=np.gcd.reduce(arr)    #y=1
print(x, y)