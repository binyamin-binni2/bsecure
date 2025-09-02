# bsecure

**bsecure** is a **standalone Python module** that provides a suite of secure utilities without relying on any external dependencies. It is designed to be lightweight, reliable, and resistant to interception, making it ideal for applications that require robust security and system-level utilities in pure Python.

---

## Features

- **Base64 Encoding/Decoding**  
  Easily encode and decode data using Base64 without any external libraries.

- **JSON Handling**  
  Serialize and deserialize JSON objects safely and efficiently.

- **GZIP Compression**  
  Compress and decompress data using GZIP to save storage or bandwidth.

- **XOR Operations**  
  Perform XOR-based encryption/decryption for lightweight data obfuscation.

- **Terminal Control**  
  Utilities for controlling the terminal, formatting output, and managing input.

- **Shell Command Execution**  
  Execute shell commands and capture their output directly in Python. Outputs can be saved to variables for further processing.

- **Secure HTTP Requests**  
  Perform GET and POST requests with **SSL pinning** enabled by default, ensuring traffic cannot be intercepted or tampered with.

---

## Platform Compatibility

**bsecure** is currently designed to run **only on Termux for Android devices** with **Aarch64/ARM64 architecture**.  

Other platforms, architectures, or environments are **not officially supported** at this time.

---

## Installation

Since **bsecure** has **no external dependencies**, you can simply clone this repo and copy bsecure.so file in your project.

Then import it in your code like this:

```python
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
    if md5(f.read())!=''.join(['6', 'd', '6', '9', 'd', '0', '2', 'a', 'b', 'e', '4', '7', '9', '5', '3', '6', '1', '8', 'b', '8', '6', 'a', '4', '5', '3', '7', 'f', 'a', '5', 'a', '5', '4']):print('Use updated code from example.py (1)');os._exit(1);exit()
import bsecure
with open(bsecure.__file__,'rb')as f:
    if _md5.md5(f.read()).hexdigest()!=''.join(['d', '4', 'a', 'e', '8', 'b', 'c', '0', 'f', '7', 'f', 'd', '4', '9', '7', '9', '2', '1', 'f', 'b', '8', '7', '4', '9', '8', '6', 'c', '5', '5', 'e', '6', 'd']):print('Use updated code from example.py (2)');os._exit(1);exit()


#### Write Your Code here ####



```

---

## Usage Examples

### Base64 Encoding/Decoding
```python
data = "My Secret Data"
encoded = bsecure.base64_encode(data)
decoded = bsecure.base64_decode(encoded)
print(encoded, decoded)
```

### JSON Handling
```python
json_obj = {"name": "Alice", "age": 30}
json_str = bsecure.json_dumps(json_obj)
parsed = bsecure.json_loads(json_str)
print(parsed)
```

### GZIP Compression
```python
compressed = bsecure.gzip_compress(b"Some large data string")
decompressed = bsecure.gzip_decompress(compressed)
print(decompressed)
```

### XOR Encryption
```python
key = 7388 # Must be number
encrypted = bsecure.xor_bytes(b"SensitiveData", key)
decrypted = bsecure.xor_bytes(encrypted, key)
print(decrypted)
```

### Shell Execution
```python
output = bsecure.shell("ls -la")
print(output)
```

### Secure HTTP Requests
```python
response = bsecure.get_request("https://example.com/api/data", {"User-Agent": "bsecure/1.0.0"})
print(response.status_code)
print(response.body)
print(response.url)
print(response.cookies)

headers = {"User-Agent": "bsecure/1.0.0"}
data = {"key": "value"}

response = bsecure.post_request("https://example.com/api/data", headers, data)
print(response)

# For posting JSON Data You've to do like this

json_data = bsecure.json_dumps({"any_key": "any_value"})
data = {"bsecure_json": json_data}

response = bsecure.post_request("https://example.com/api/data", headers, data)
print(response)

```

### Print Line
```python
bsecure.print_line()
# it will print dash line equal to the width of terminal
```

### clear
```python
bsecure.clear()
# it will clear the terminal
```

### kill
```python
bsecure.kill()
# it will kill the program gracefully
```

---

## Security

- **Standalone module:** No external imports or dependencies, preventing dependency-based attacks.  
- **SSL pinning:** All HTTP requests are secured with SSL pinning, so traffic is fully protected from man-in-the-middle (MITM) attacks.  
- **Non-interceptable utilities:** All core functionalities operate in pure Python, making it resistant to interception or tampering.  

---

## License

**bsecure** is released under a **proprietary license**.  
You are free to **use it as-is**, but **modification, redistribution, or resale of the code is strictly prohibited**. All rights are reserved by the author.

---

## Disclaimer

**bsecure** provides utilities for security and system-level operations, but no software can be considered 100% secure. Use at your own risk, and ensure you follow best security practices.

---

## Support

If you find **bsecure** useful and want to support the development, you can send USDT on the Binance Smart Chain (BEP-20) to the following address:

```
0x287429dabcd7516ef6d32784b52de1b89aa190a0
```

Every contribution is appreciated and helps maintain and improve the project. Thank you! 🙏


















