from network import Sigfox
import ubinascii
 
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
 
print("ID ", ubinascii.hexlify(sigfox.id()))
print("PAC ", ubinascii.hexlify(sigfox.pac()))
