import subprocess
hostname = subprocess.check_output("hostname")
hostname = 'res/'+hostname.split('\n')[0]
import time
while True:
    hosts = subprocess.check_output("nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits", shell=True)
    hosts = hosts.split('\n')
    import numpy as np
    hosts = np.array(hosts[:-1]).astype(int)/ 1000
    
    import pickle
    for trycnt in range(10):
        if trycnt >= 7:
            raise Exception("unable towrite")
        try:
            with open(hostname, 'wb') as f:
                pickle.dump(hosts, f)
        except:
            time.sleep(1)
            continue
        break
    time.sleep(5)
