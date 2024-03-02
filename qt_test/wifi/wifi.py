import subprocess
import re

#执行通过subprocess check_output执行指令
result = subprocess.check_output(["netsh", "wlan", "show", "network"])

# with open("./qt_test/wifi/wifi.txt", "r" ,errors='ignore') as f:
#     s = f.read()
#     print(s.decode("gbk"))
# print(result.decode("gbk",errors="ignore"))
# print(result)
from urllib import parse
str2 = b'SSID 7 : \xe5\x8d\xb7\xe4\xbc\x9a\xe5\x90\xa7\xef\xbc\x8c\xe5\x88\xab\xe7\x9c\x9f\xe8\x80\x83\xe4\xb8\x8d\xe4\xb8\x8a\xe4\xba\x86\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n  \
  \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\n \
  SSID 8 : zzuli-inside\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : \xbf\xaa\xb7\xc5\xca\xbd\r\n    \xbc\xd3\xc3\xdc                    : \xce\xde \r\n\r\n \
    SSID 9 : zzb\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\n \
        SSID 10 : \xe5\xb0\x8f\xe5\xa4\x8f\xe5\x90\x8c\xe5\xbf\x97\xe7\x9a\x84wifi\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\n \
            SSID 11 : \xe6\x96\xaf\xe5\xa1\x94\xe6\x99\xae\xe8\xbe\xa3\xe9\x85\xb1\xef\xbc\x8c\xe7\xa0\xb8\xe7\x93\xa6\xe9\xb2\x81\xe5\xa4\x9a\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\n \
                SSID 12 : DIRECT-WGEXDSXQXImswO\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc \
          : CCMP \r\n\r\nSSID 13 : \xe5\xbe\xa1\xe7\x94\xa8WiFi\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\nSSID 14 : Redmi K60 Ultra\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc \
         : CCMP \r\n\r\nSSID 15 : iPhone 15 Pro Max\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4        \
         : WPA3 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\nSSID 16 : 404_m6200\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\nSSID 17 : HONOR 90 Pro\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA3 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\nSSID 18 : 404\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\nSSID 19 : OnePlus Ace 2\r\n    Network type            : \xbd\xe1\xb9\xb9\r\n    \xc9\xed\xb7\xdd\xd1\xe9\xd6\xa4                : WPA2 - \xb8\xf6\xc8\xcb\r\n    \xbc\xd3\xc3\xdc                    : CCMP \r\n\r\n'

str1 =b'\xe5\x8d\xb7\xe4\xbc\x9a\xe5\x90\xa7\xef\xbc\x8c\xe5\x88\xab\xe7\x9c\x9f\xe8\x80\x83\xe4\xb8\x8d\xe4\xb8\x8a\xe4\xba\x86\r\n'
str3 = b"\xbd\xd3".decode("gbk")

pattern = re.compile(r'SSID(.*?)(\r\n)')    
m = pattern.finditer(str2.decode("utf-8",errors="ignore"))
for mm in m:
    print(mm)
# print(str1)
str4 = b"\x99"
# \xe5\xb0\x8f
# \xe6\xb1\e5
# \xa1\x94\xe6
# \x99\xae\xe8
# \xbe\xa3\xe9
# \x85\xb1\xef
# \xbc\x8c\xe7
# \xa0\xb8\xe7
# \x93\xa6\xe9
# \xb2\x81\xe5
# \xa4\x9a
# s =  str2.decode('gbk', errors = "replace")
# ss = s.decode()
# s = str(str1)
# print(str2.decode("gbk",errors="ignore"))
def decode_mixed_encoding(input_bytes):
    text = ""
    i = 0
    print(len(input_bytes))
    while i < 32:
        # print(input_bytes[i],end="\n")
        if input_bytes[i] < 128:  # ASCII
            text += chr(input_bytes[i])
            i += 1
            # print(text,i,end="\n")
        else:  # Non-ASCII

            try:
                text += input_bytes[i:i+2].decode('gbk')
                # print(input_bytes[i:i+2],input_bytes[i:i+2].decode('gbk'))
                i += 2
            except UnicodeDecodeError:
                try:
                    text += input_bytes[i:i+3].decode('utf-8')
                    # print(text,"-",input_bytes[i:i+3],input_bytes[i:i+3].decode('utf-8'),end="\n")
                    i += 3
                except UnicodeDecodeError:
                    text += '?'
                    print(text,i,end="\n") 
                    i += 1
    # print(text) 
# decode_mixed_encoding(str1)
# result = result.decode("gbk",errors="ignore")
# print(result)
# lst = result.split("\r\n")
# lst = lst[4:]

# for index in range(len(lst)):
#     # if index % 5 == 0:
#     print(lst[index])


