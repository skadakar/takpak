import time
#from time import sleep,gmtime,strftime
import os
import uuid
#from socket import getfqdn
import socket 

#import takcot. Note this only works if you have installed the package
#   If you have not installed as a package, you may have to tune your imports
#   to be local to where your source is
from takpak.mkcot import mkcot
from takpak.takcot import takcot

#logging.basicConfig(level=logging.INFO) # level=10

TAK_IP = '172.16.30.30'
TAK_PORT = 8087

#TAK_IP = os.getenv('ATAK_IP', '204.48.30.216')
#TAK_PORT = int(os.getenv('ATAK_PORT', '8087'))

#-----------------------------------------------------------------------------------------


# substantiate the class
takserver = takcot()

# Now open server
print("Opening TAK Server")
testsock = takserver.open(TAK_IP)

#print("open return is:")
#print(testsock)


print()
print("send a connect")
takserver.flush()  # flush the xmls the server sends
#print(takserver.read())  # read all the server CoT's, will send last + the connct

connect_xml = mkcot.mkcot(cot_type="t", cot_how="h-g-i-g-o")
print("Connect XML is:")
print(connect_xml)

# send the connect string, server does not echo
takserver.send(mkcot.mkcot(cot_type="t", cot_how="h-g-i-g-o")) 
# send the connect string, server does not echo

#time.sleep(5)
print("read the Connect response")
print(takserver.read())  # read all the server CoT's, will send last + the connct

#print("Flush the server response")
#takserver.flush()  # flush the xmls the server sends
#time.sleep(3)

#for i in range(10):
while True:
    print()

    print("wait for a server CoT")
    print(takserver.read(readtimeout=10))
    time.sleep(0.1)

# Always need to close out the connection
# good practice to include reading anything the server pushed
# to prevent broken pipe errors on the server

#takserver.flush()  # flush the xmls the server sends

print("Closing TAK Server")
takserver.close()


