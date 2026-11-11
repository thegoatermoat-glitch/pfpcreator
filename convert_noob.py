# Usage: python3 convert_noob.py RobloxNoobRig.proj public/noob.json
import sys, json, math
from convert_noob_mp import R
top=R(open(sys.argv[1],'rb').read(),4).read(); nodes={n[0]:n for n in top[1]}; meshes={m[0]:m for m in top[3]}
J=lambda x:json.loads(x[1])
def lp(n):
    for sec in n[2]:
        if sec[0][1]==b'PTransform':
            for k,v,_ in sec[1]:
                if k[1]==b'localPosition': j=J(v); return [j['x'],j['y'],j['z']]
    return [0,0,0]
def world(i):
    p=[0,0,0]
    while i!=-1:
        l=lp(nodes[i]); p=[a+b for a,b in zip(p,l)]; i=nodes[i][3]
    return p
def mesh_id(n):
    for sec in n[2]:
        if sec[0][1]==b'PMeshRenderer':
            for k,v,_ in sec[1]:
                if k[1]==b'pMesh': return J(v)['id']
parts=[]
for n in top[1]:
    mid=mesh_id(n)
    if mid is None: continue
    m=meshes[mid]; idx,uv,P,N=m[4],m[5],m[6],m[3]; off=world(n[0]); piv=world(n[3])
    smooth=len(idx)//3>100; acc={}
    if smooth:
        for t in range(len(idx)//3):
            for k in range(3): a=acc.setdefault(idx[3*t+k],[0,0,0]); [a.__setitem__(c,a[c]+N[t][c]) for c in range(3)]
    pos=[];nr=[];uvs=[]
    for c in range(len(idx)):
        p=P[idx[c]]; pos+= [round(p[i]+off[i]-piv[i],4) for i in range(3)]
        v=N[c//3]
        if smooth:
            a=acc[idx[c]]; l=math.sqrt(sum(x*x for x in a)) or 1; v=[x/l for x in a]
        nr+=[round(x,3) for x in v]; uvs+=[round(uv[c][0],4),round(uv[c][1],4)]
    parts.append({'n':n[1][1].decode(),'piv':[round(x,4) for x in piv],'pos':pos,'uv':uvs,'nrm':nr})
json.dump(parts,open(sys.argv[2],'w'),separators=(',',':'))
print([(p['n'],p['piv'],len(p['pos'])//9) for p in parts])
