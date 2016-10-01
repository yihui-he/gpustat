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
    with open(hostname, 'wb') as f:
        pickle.dump(hosts, f)

    time.sleep(5)
