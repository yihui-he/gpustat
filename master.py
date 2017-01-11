import os.path as osp
import os 
import pickle
import pandas as pd
import time
from IPython import embed

res = 'res'
starttime=0
removemachines=False
while True:
    if time.time()>starttime+3600:
        starttime=time.time()
        removemachines = True
    machines = sorted(os.listdir(res))
    s = []
    for machine in machines:
        if removemachines:
            os.remove(osp.join(res,machine))
            continue
        while True:
            try:
                with open(osp.join(res, machine), 'rb') as f:
                    a = pickle.load(f)
                success = True
            except:
                success = False
            if success:
                break

        a = pd.Series(a)
        a.name = machine
        s.append(a)
    df = pd.DataFrame(s)
    df['>6'] = (df>=6).sum(axis=1)
    print '\n'
    print df
    os.system('rm res/*')
    time.sleep(5)
    removemachines=False
        
