from base64 import b64decode, decode
import struct


def main():
  f = open("hideandseek.png", "rb").read()[8:]
  
  i = 0
  res = b""
  while True:
    l = struct.unpack(">I", f[i:i+4])[0]
    t = f[i+4:i+8]
    c = f[i+8:i+8+l]
    i += 12 + l

    if (t == b"IEND"):
      break
    
    if (t == b'eDIH'):
      print(t, c)
      res += c
  print(b64decode(res))

if __name__ == "__main__":
  main()