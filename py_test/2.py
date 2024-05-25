# 1导包 
import socket

# 2初始化套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3建立链接  要传入链接的服务器ip和port
tcp_socket.connect(('127.0.0.1', 11000))

# 4发数据
tcp_socket.send('哈哈呵呵呵'.encode('utf-8'))

# 5断开
tcp_socket.close()

