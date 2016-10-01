import os.path as osp
import os 
import pickle
import pandas as pd
import time
from IPython import embed

res = 'res'
while True:
    machines = os.listdir(res)
    s = []
    for machine in machines:
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
    print df
    print '\n'
    time.sleep(5)
        