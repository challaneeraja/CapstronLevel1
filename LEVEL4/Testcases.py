import pytest
from LEVEL3.demo_oop import SystemDrive
from LEVEL3.demo_exception import FileSearcher
class  Test_Drive:
    def test_drivecase(self):
        obj=SystemDrive()
        self.expected=obj.find_drive()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileSearcher()
        d=obj.search('c','data2.txt')
        self.expected_filename=d[0]
        self.actual_res='c:\\neeru\\data2.txt'
        assert self.expected_filename==self.actual_res
