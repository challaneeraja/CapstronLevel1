from .import demo_drive as dd
import os
def search_file(name,path):
    for i in path:
        for root,dirs,files in os.walk(i):
            for j in files:
                if j==name:
                    print("file found")
                    print(root)
                    break
name=input("enter the filename:")
path=dd.GetDrive()
search_file(name,path)