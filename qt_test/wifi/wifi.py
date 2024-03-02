import subprocess

result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
result = result.decode('gbk')  # 注意编码，根据你的电
print(result)