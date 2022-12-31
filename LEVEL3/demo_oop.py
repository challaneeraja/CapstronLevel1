import os
class SystemDrive:
    def __init__(self):
        pass
    def find_drive(self):
        drives=[]
        for x in range(65,69):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives


if __name__=='__main__':
    obj=SystemDrive()
    print(obj.find_drive())


