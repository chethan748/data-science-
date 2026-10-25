import multiprocessing  
from concurrent.futures import ThreadPoolExecutor
import time

## mutliprocessing with process lpoll executor
from concurrent.futures import ProcessPoolExecutor
def print_num2():
    for i in range(5):
        time.sleep(1)
        print(f"Number : {i}")
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        res=executor.map(print_num2())
for r in res:
    print(r)