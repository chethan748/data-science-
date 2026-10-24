import multiprocessing  
import time
def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(letter)
t=time.time()
if __name__=="__main__":
##creating 2 thread  
    t1=multiprocessing.Process(target=print_num)
    t2=multiprocessing.Process(target=print_letter)

    t=time.time()
    t1.start()
    t2.start()
    ## wiat for the threads to complete 
    t1.join()
    t2.join()
    finished_time=time.time()-t
    print(finished_time)


import multiprocessing  
import time
def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(letter)
t=time.time()
if __name__=="__main__":
##creating 2 thread  
    t1=multiprocessing.Process(target=print_num)
    t2=multiprocessing.Process(target=print_letter)

    t=time.time()
    t1.start()
    t2.start()
    ## wiat for the threads to complete 
    t1.join()
    t2.join()
    finished_time=time.time()-t
    print(finished_time)

    print(finished_time)