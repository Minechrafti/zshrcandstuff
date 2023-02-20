import os
import sys

def getType(string):
    for i in range(len(string)):
        if(string[i] == '.'):
            return string[i:]


file = str(sys.argv[1])
ending = getType(file)
if(ending[0] != '.'):
    exe = './' + file
    os.system(exe)
if(ending == '.sh'):
    print("Executing bash file...")
    exe = 'chmod 755 ' + file + '; ./' + file
    os.system(exe)
if(ending == '.py'):
    print("Executing python file...")
    exe = 'python3 ' + file
    os.system(exe)



