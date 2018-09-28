import sys
import pexpect

user = 'pi'
password = 'clusterhat'
host = 'p1.local'
fout = open('mylog.txt', 'wb')

def dossh(user, password, host):
  try:
    child = pexpect.spawn('ssh %s@%s' % (user,host))

    child.logfile = sys.stdout
    child.logfile_send = fout

    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('python Capture.py')
    
    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('gcc -o Analyze Analyze.c'
                   
    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('./Analyze')
    
    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('cat /home/pi/pixels.txt')
    #child.sendline('scp /home/pi/pixels.txt')
    
    child.close()
    
  except Exception as error:
    print "Errors otw"
    print error
    sys.exit
  


dossh(user, password, host)
