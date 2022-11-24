import time, datetime, os

basedir = "C:\Local_Data"
timesdir = "times"
totaltime = 0.0

directories = os.listdir(basedir + "\\" + timesdir)
print(directories)

def returntime(filename):
    with open(filename, 'r') as f:
        text = f.read().strip().split("###")
        text.pop(-1)
        return text[-1]

for i in directories:
    
    time = returntime(basedir + "\\" + timesdir + "/" + i)
    totaltime = totaltime + float(time)

print(totaltime)
input()