from time import perf_counter
from threading import Thread
from locate_drive.demo_drive import GetDrive
from locate_drive.demo_file1 import search_file
start_time=perf_counter()
name=input("enter the file name ")
path=input(" enter the path ")
t1=Thread(target=GetDrive)
t2=Thread(target=search_file(name,path))
t1.start()
t2.start()
t1.join()
t2.join()
end_time=perf_counter()
print(f'{end_time-start_time} seconds return')