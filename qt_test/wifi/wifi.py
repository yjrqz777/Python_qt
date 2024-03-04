import subprocess
import re

#执行通过subprocess check_output执行指令
result = subprocess.check_output(["netsh", "wlan", "show", "network"])


pattern = re.compile(r'SSID (?:[1-9]|[1-9]\d) :(.*?)\r\n')    
m = pattern.findall(result.decode("utf-8",errors="ignore"))
print(len(m),m)
# print(m[0][1])
for mm in m:
    print(mm)

