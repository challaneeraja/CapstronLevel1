import logging
class DemoFile():
    def __init__(self):
        logging.basicConfig(filename="filelog1.txt",level=logging.WARNING)
    def Fileopen(self):
        try:
            f=open("text","r")
        except FileNotFoundError as msg:
            logging.exception(msg)
if __name__=='__main__':
    obj=DemoFile()
    obj.Fileopen()