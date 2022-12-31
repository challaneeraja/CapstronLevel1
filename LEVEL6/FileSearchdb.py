import os
import threading
import logging
from LEVEL3.demo_exception import FileSearcher
from searchdb import SearchDB
from LEVEL5.demo_logdb import searchlog
# class FileSearch(threading.Thread):
#     # drive=""
#     # file_name=""
#     def __init__(self):
#         super().__init__()
#         self.drive = ""
#         self.file_name = ""
#     def search(self,drives,file_name):
#         try:
#             print("this is file serch:")
#             file_paths=[]
#             drv=drives+":\\"
#             print(drv)
#             for root,dirs,files in os.walk(drv):
#                 for name in files:
#                     if name==file_name:
#                         path=os.path.abspath(os.path.join(root,name))
#                         file_paths.append(path)
#                         self.search(self,drive,file_name)
#         except:
#             print("there was an error")
#         return file_paths
#
#     def run(self):
#
#         self.search(self.drives,self.file_name)
if __name__=='__main__':
    data=[]
    drive=input("enter drive")
    file_name=input("enter file name")
    obj=FileSearcher()
    dbobj=SearchDB()
    searchLg=searchlog()
    res=dbobj.searchdb(file_name)

    if res==0:
        data=obj.search(drive,file_name)
        print(data)
        # dbobj.insertDB(data)
        try:
            print(data[0])
            dbobj.insertDB(data[0])
            logging.info(data[0])
        except IndexError:
            print("no file exists")

    else:
        print(res)
# '''import os
# import threading
# from searchdb import SearchDB
# class FileSearcher(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.s=""
#     def task2(self,drive,s):
#         try:
#             c=0
#             for root,dirs,files in os.walk(drive):
#                 for name in files:
#                     filepath=os.path.join(root,name)
#                     if s in name:
#                         c=c+1
#                         return filepath
#             if c==0:
#                 print("file not found")
#             else:
#                 print(f"{c} files.")
#         except:
#             print("No error")
#     def run(self):
#         pass
# if __name__=='__main__':
#     drive,file=input("drive name"),input("file name")
#     obj=FileSearcher()
#     dbobj=SearchDB()
#     res=dbobj.searchdb(file)
#     if res==0:
#         data=obj.task2(drive,file)
#         print(data)
#         dbobj.insertDB(data)
#     else:
#         print(res)''''''