import paramiko

def ssh_command(ip, port, user, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=password,)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print ('-----OUTPUT--------')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    #user = get.pass.getuser
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('ENTER SERVER IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter Command or <CR>:') or 'id'
    ssh_command(ip, port, user, password, cmd)
