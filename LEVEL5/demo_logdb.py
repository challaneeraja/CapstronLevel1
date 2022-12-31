import re
import logging
class searchlog():
    def __init__(self):
        logging.basicConfig(filename="file1.txt",level=logging.INFO)
    def dbsearchlog(self,filename):
        file=open("file1.txt","r")
        str="text_file1"
        data=re.compile(str)
        res=data.search(str)
        line=file.readline()
        print(res.group(0))
