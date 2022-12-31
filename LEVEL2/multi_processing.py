import multiprocessing as mp
from locate_drive.demo_drive import GetDrive
from locate_drive.demo_file1 import search_file
from time import perf_counter
def drive():
    GetDrive()
def searchfile(name,path):
    search_file(name,path)
if __name__=='__main__':
    start_time=perf_counter()
    print("Number of processors:",mp.cpu_count())
    name=input("enter the file name:")
    path=input("enter the path")
    p1=mp.Process(target=drive)
    p2=mp.Process(target=searchfile,args=(name,path))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time=perf_counter()
    print(f'{end_time-start_time} seconds taken')
