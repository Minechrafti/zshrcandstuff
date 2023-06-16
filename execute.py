import os
import sys

def getType(string):
    return '.' + string.split('.')[1]
    for i in range(len(string)):
        if(string[i] == '.'):
            return string[i:]


file = str(sys.argv[1])
ending = getType(file)
if(not ending.__contains__('.')):
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
if(ending == '.c'):
    print("Executing c file...")
    exe = f'gcc {file} -o ./tmp; ./tmp; rm ./tmp'
    os.system(exe)
if(ending == '.java'):
    print("Trying to execute java")
    exe = f'javac {file}'
    os.system(exe)


