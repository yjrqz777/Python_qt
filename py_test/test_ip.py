# -*- coding: utf-8 -*-
'''
@File    :   test_ip.py
@Time    :   2024/03/16 09:47:00
@Author  :   YJRQZ777
@Version :   1.0
@Contact :   3210551161@qq.com
'''



# str_ip = "192.168.179.170"
# str_ip1 = str_ip.split('.')[0]
# str_ip2 = str_ip.split('.')[1]
# str_ip3 = str_ip.split('.')[2]
# str_ip4 = str_ip.split('.')[3]

# if __name__ == '__main__':
#     s = ' '.join(str_ip1)  
#     s1 = ' '.join(str_ip2)
#     s2 = ' '.join(str_ip3)
#     s3 = ' '.join(str_ip4)
#     print(s+"."+s1+"."+s2+"."+s3)
#     print(s)
#     # # print(str.split('.')[0]==192)
#     # print(str[:7])
#     # print(str)
import os  
  
dir_name = 'picture'  
if not os.path.exists(dir_name):  
    os.mkdir(dir_name)  
else:  
    print(f"Directory '{dir_name}' already exists.")
