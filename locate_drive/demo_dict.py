import os
d="C://Pytestcapstronproject"
di={}
for root,dir,files in os.walk(d):
    for d in dir:
        di[d]=os.listdir(root+"/"+d)
print(di)