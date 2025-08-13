_B='d'
_A='3'
s=[7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22,5,9,14,20,5,9,14,20,5,9,14,20,5,9,14,20,4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21]
K=[3614090360,3905402710,606105819,3250441966,4118548399,1200080426,2821735955,4249261313,1770035416,2336552879,4294925233,2304563134,1804603682,4254626195,2792965006,1236535329,4129170786,3225465664,643717713,3921069994,3593408605,38016083,3634488961,3889429448,568446438,3275163606,4107603335,1163531501,2850285829,4243563512,1735328473,2368359562,4294588738,2272392833,1839030562,4259657740,2763975236,1272893353,4139469664,3200236656,681279174,3936430074,3572445317,76029189,3654602809,3873151461,530742520,3299628645,4096336452,1126891415,2878612391,4237533241,1700485571,2399980690,4293915773,2240044497,1873313359,4264355552,2734768916,1309151649,4149444226,3174756917,718787259,3951481745]
def left_rotate(x,c):return(x<<c|x>>32-c)&4294967295
def md5(message):
    D=bytearray(message);P=len(D)*8;D.append(128)
    while len(D)*8%512!=448:D.append(0)
    D+=P.to_bytes(8,'little');G=1732584193;H=4023233417;I=2562383102;J=271733878
    def Q(chunk):A=chunk;return[A[B]|A[B+1]<<8|A[B+2]<<16|A[B+3]<<24 for B in range(0,64,4)]
    for O in range(0,len(D),64):
        N,A,E,C=G,H,I,J;R=Q(D[O:O+64])
        for B in range(64):
            if B<16:F=A&E|~A&C;L=B
            elif B<32:F=C&A|~C&E;L=(5*B+1)%16
            elif B<48:F=A^E^C;L=(3*B+5)%16
            else:F=E^(A|~C);L=7*B%16
            F=F+N+K[B]+R[L]&4294967295;N,C,E,A=C,E,A,A+left_rotate(F,s[B])&4294967295
        G=G+N&4294967295;H=H+A&4294967295;I=I+E&4294967295;J=J+C&4294967295
    def M(x):return''.join(hex(x>>A*8&255)[2:].rjust(2,'0')for A in range(4))
    return M(G)+M(H)+M(I)+M(J)
import sys,os
sys.path.append(os.path.dirname(__file__))
import _md5
with open(_md5.__file__,'rb')as f:
    if md5(f.read())!=''.join(['8','0',_B,'4','4',_B,'5','8','e',_A,_B,'5','c','7','9',_A,_A,'f','e','a','f','e','b','8',_B,_A,_B,'6','f','2',_A,'5']):print('Use updated code from example.py (1)');os._exit(1);exit()
import bsecure
with open(bsecure.__file__,'rb')as f:
    if _md5.md5(f.read()).hexdigest()!=''.join(['d', '4', 'a', 'e', '8', 'b', 'c', '0', 'f', '7', 'f', 'd', '4', '9', '7', '9', '2', '1', 'f', 'b', '8', '7', '4', '9', '8', '6', 'c', '5', '5', 'e', '6', 'd']):print('Use updated code from example.py (2)');os._exit(1);exit()


#### Write Your Code here ####


headers = {
    "User-Agent": "BSecure/1.0.0"
}

req = bsecure.get_request("https://graph.facebook.com/1348564698517390", headers)

body = req.body

json_decoded_body = bsecure.json_loads(body)

print(json_decoded_body["name"])
