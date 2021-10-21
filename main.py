import os
import shutil
import time

time.time()
path="/WhiteHat Junior/Project 99"
pathExists=os.path.exists(path)
walk=os.walk(path)
#print(walk)
#print(os.path.join(path,"a","a.txt"))
ctime=os.stat(path).st_ctime
#print(ctime)
if(ctime>70):
    os.remove("/WhiteHat Junior/Project 99/a.txt")
else:
    print("Not Found Message")