

f = open("mapping.txt", "r")
lines = f.readlines()
g = open("newmapping.txt", "w")

for x in lines:
    x=x.strip()
    print(x)
    arr = x.split()
    if not arr[0].startswith('20'):
        continue
    
    if arr[1] == 'Ms.':
        arr[1]=arr[2]
    
    if len(arr)>2:
        arr=arr[:2]
        
    g.write(arr[0]+" "+arr[1]+"\n")
    
f.close()
g.close()