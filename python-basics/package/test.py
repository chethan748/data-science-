
'''real world example : multiprocessing for cpu bound taks senario : factorial calculation 
espcially for large number invloving significant work Multiple processes can distribute the 
workload across multiple CPU cores, improving performance. '''

import multiprocessing

import math
import sys
import time 
##Increase the maximum number of digits for integer conversion. 
sys.set_int_max_str_digits(50000)
##function To compute the factorial of a given number
def computer_factorial(number):
    print(f"computing factorial of {number }")
    res=math.factorial(number) 
    return res
if __name__=="__main__":
    num=[5000,6000,7000,8000,9000]
    #create a poll of worker process 
    with multiprocessing.Pool() as pool:
        res=pool.map(computer_factorial,num)
    
    for number, result in zip(num, res):
        print(f"Factorial of {number} = {result}")   
        print(f"Factorial of {number} has {len(str(result))} digits")
        
t1=time.time()
t2=time.time()
print(t2-t1)