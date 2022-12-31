from demo_exception import FileSearcher
from threading import Thread
class SearchManager:
    def __init__(self):
        pass
    def search1(self,file_name,drives):
        print("this is a search method for searchmanager")
        search_thread=[]
        file_searchers=[]
        for drive in drives:
            print(drive)
            file_searcher=FileSearcher()
            file_searcher.search(drive, file_name)
            search_threads=Thread()
            search_threads.start()
            file_searchers.append(file_searcher)
            search_thread.append(search_thread)
        for search_thread in search_thread:
            search_threads.join()
        search_results=[]
        for file_searcher in file_searchers:
            search_results.append(file_searcher.file_name)
        return search_results
if __name__=='__main__':
    obj=SearchManager()
    d=obj.search1("demo.txt","C")
    #d1=obj.search("text_file1","D://")
    print(d)
    #print(d1)