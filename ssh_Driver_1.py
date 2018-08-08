#import pexpect
import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = raw_input('password: ')

    s.login(hostname, username, password)
    #COMMAND LINE ENTRY = sendline
    s.sendline('uptime')
    s.prompt()
    print s.before()

    s.sendline('ls')
    s.prompt()
    print s.before()

    s.sendline('python testCamera.py')
    s.prompt()
    print s.before()
    s.logout()

except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login"
    print str(e)
