import struct
class R:
    def __init__(s,d,o=0): s.d=d;s.o=o
    def u(s,n): v=s.d[s.o:s.o+n]; s.o+=n; return v
    def read(s):
        b=s.d[s.o]; s.o+=1
        if b<=0x7f: return b
        if b>=0xe0: return b-256
        if 0xa0<=b<=0xbf: return ('str',s.u(b&31))
        if 0x90<=b<=0x9f: return [s.read() for _ in range(b&15)]
        if 0x80<=b<=0x8f: return {('k',i):(s.read(),s.read()) for i in range(b&15)}
        if b==0xc0: return None
        if b==0xc2: return False
        if b==0xc3: return True
        if b in(0xc4,0xd9): return ('bin' if b==0xc4 else 'str',s.u(s.u(1)[0]))
        if b in(0xc5,0xda): return ('bin' if b==0xc5 else 'str',s.u(struct.unpack('>H',s.u(2))[0]))
        if b in(0xc6,0xdb): return ('bin' if b==0xc6 else 'str',s.u(struct.unpack('>I',s.u(4))[0]))
        if b==0xca: return struct.unpack('>f',s.u(4))[0]
        if b==0xcb: return struct.unpack('>d',s.u(8))[0]
        if b==0xcc: return s.u(1)[0]
        if b==0xcd: return struct.unpack('>H',s.u(2))[0]
        if b==0xce: return struct.unpack('>I',s.u(4))[0]
        if b==0xcf: return struct.unpack('>Q',s.u(8))[0]
        if b==0xd0: return struct.unpack('>b',s.u(1))[0]
        if b==0xd1: return struct.unpack('>h',s.u(2))[0]
        if b==0xd2: return struct.unpack('>i',s.u(4))[0]
        if b==0xd3: return struct.unpack('>q',s.u(8))[0]
        if b==0xdc: n=struct.unpack('>H',s.u(2))[0]; return [s.read() for _ in range(n)]
        if b==0xdd: n=struct.unpack('>I',s.u(4))[0]; return [s.read() for _ in range(n)]
        if b==0xde: n=struct.unpack('>H',s.u(2))[0]; return {('k',i):(s.read(),s.read()) for i in range(n)}
        raise ValueError(hex(b)+' at '+str(s.o-1))
