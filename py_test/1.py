# -*- coding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2024/03/16 10:17:55
@Author  :   YJRQZ777
@Version :   1.0
@Contact :   3210551161@qq.com
'''


s = 'abcd'
c = ' '
s_list = list(s)
i = s_list.index(c)
s_list.insert(i,c)
s = ''.join(s_list)
print(s)