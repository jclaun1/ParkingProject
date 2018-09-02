import sys
import pexpect

#user = 'pi@p1.local'
#host = '10.0.0.139'
user = 'pi'
password = 'clusterhat'
host = 'p1.local'
lsCommand = 'ls'
fout = open('mylog.txt', 'wb')

def dossh(user, password, host):#, command):
  try:
    child = pexpect.spawn('ssh %s@%s' % (user,host))
    child.logfile = sys.stdout
    child.logfile_send = fout
    prompt = child.expect(['password:', r"yes/no", "pi@p1", pexpect.EOF])
    child.sendline(lsCommand)
    lsVal = child.expect(['pi@p1', pexpect.EOF])
    print lsVal
    child.sendline('raspistill -vf -hf -o TestPic.jpg')
    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('scp /home/pi/TestPic.jpg pi@10.0.0.183:/home/pi/')
    child.sendline(password)
    found = child.expect(['pi@', pexpect.EOF])
    print found
    child.sendline(password)
    child.expect(['pi@p1.local', pexpect.EOF])
    child.sendline('python zzTest.py')
    child.expect(['We', pexpect.EOF])
    print
    print
    child.expect(['pi@p1', pexpect.EOF])
    child.sendline('raspistill -vf -hf -o TestPic.jpg')
    child.expect(['pi@p1', pexpect.EOF])

    if prompt == 0:
      child.sendline(password)
      found = child.expect(['pi@p1.local', 'pi@p1:', 'local', pexpect.EOF])      
      child.sendline(lsCommand)
      
    elif prompt == 1:
      print "Prompt = 1"
      child.sendline("yes")
      child.expect("password:", timeout=30)
      child.sendline(password)
      data = child.read()
      print data
      child.close()
    
  except Exception as error:
    print "Errors otw"
    print error
    sys.exit
  


dossh(user, password, host)
