import sys
import pexpect

user = 'pi@p1.local'
password = ''
host = 'parkingpalpi.hopto.org'
command = 'hostname ; echo $?'

def dossh(user, password, host, command):
  child = pexpect.spawn('ssh %s@%s %s' % (user,host,command),logfile=sys.stdout,timeout=None)
  prompt = child.expect(['password:', r"yes/no",pexpect.EOF])
  
  if prompt == 0:
    child.sendline(password)
  elif prompt == 1:
    child.sendline("yes")
    child.expect("password:", timeout=30)
    child.sendline(password)
    data = child.read()
    print data
    child.close()

dossh(user, password, host, command)
