import numpy as np
import uuid

prob = 0.5

f = open("mapping5.txt", "r")
lines = f.readlines()

for x in lines:

    if np.random.random() > prob:
        continue
    x=x.strip()
    arr = x.split()
    
    h=open(arr[0]+".pdf",'w')
    
    h.write(str(uuid.uuid4())+"\n")
    h.write(str(uuid.uuid4())+"\n")
    h.write(str(uuid.uuid4())+"\n")
    
    h.close()
    
f.close()