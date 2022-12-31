import os
import threading
class FileSearcher(threading.Thread):
    drive=""
    file_name=""
    def __init__(self):

        self.drive=""
        self.file_name=""
    def search(self,drives,file_name):
        try:
            print("this is a search method for file manager")
            file_paths=[]
            drv=drives+"://"
            print(drv)
            for root,dirs,files in os.walk(drv):
                for name in files:
                    if name==file_name:
                        # print("exists")
                        path=os.path.abspath(os.path.join(root,name))
                        file_paths.append(path)
                        self.search(self,drives,self.file_name)
                    # return file_paths
        except:
            print("file found")
        return file_paths
    def run(self):

        self.search(self.drive,self.file_name)
if __name__=='__main__':
    obj=FileSearcher()
    data=print(obj.search("C","demo.txt"))