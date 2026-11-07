# Usage: python3 convert.py Crossroads.rbxl public/scene.json
import sys, json, math, xml.etree.ElementTree as ET
BC={199:'635f62',24:'f5cd30',27:'6d6e6c',26:'1b2a35',194:'a3a2a5',192:'694028',106:'da8541',38:'a05f35',226:'fdea8d',45:'b4d2e4',102:'6e99ca',1:'f2f3f3',28:'287f47',217:'7c5c46',21:'c4281c',153:'957977',105:'e29b40',151:'78907f',107:'008f9c',37:'4b974b',23:'0d69ac',1019:'00ffff',39:'c1cade',11:'80bbdb',119:'a4bd47',5:'d7c59a',141:'27462d',29:'a1c48c',1002:'cd544b',208:'e5e4df',1027:'9ff3e9',1013:'ff00bf',196:'23478b',149:'0b1d4e',135:'74869d'}
r=ET.parse(sys.argv[1]).getroot(); ws=r.find("Item[@class='Workspace']")
f=lambda v:round(float(v),2); parts=[]; spawns=[]
for i in ws.iter('Item'):
    c=i.get('class')
    if c not in('Part','WedgePart','SpawnLocation'): continue
    p=i.find('Properties'); g=lambda n:p.find(f".//*[@name='{n}']")
    tr=float(g('Transparency').text) if g('Transparency') is not None else 0
    if tr>=1: continue
    cf=[float(e.text) for e in g('CFrame')]; sz=[f(e.text) for e in g('size')]
    t={'WedgePart':1}.get(c,0)
    if c=='Part' and g('shape') is not None: t={'0':3,'2':2}.get(g('shape').text,0)
    col=BC.get(int(g('BrickColor').text),'a3a2a5')
    parts.append([t]+[f(v) for v in cf]+sz+[col,tr])
    if c=='SpawnLocation': spawns.append([f(cf[0]),f(cf[1]+sz[1]/2),f(cf[2]),f(math.atan2(cf[5],cf[11]))])
json.dump({'p':parts,'spawns':spawns},open(sys.argv[2],'w'),separators=(',',':'))
print(len(parts),'parts',len(spawns),'spawns')
