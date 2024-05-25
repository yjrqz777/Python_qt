import socket  
import os  
import threading
def tcplink(host, port):  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:  
        # server_socket.bind((host, port))  
        # server_socket.listen(5)  
        # print('Server is listening...')  
        # client_socket, addr = server_socket.accept() 
        flag = True
        try:
            client_socket.connect((host, port)) 
            flag = True
        except Exception as e:
            flag = False
            print(e)
        print('connected')
        while flag:  
             
            # print(f'Connected by {addr}')  
    
            # 接收图片文件名  
            filename = client_socket.recv(1024).decode('utf-8').strip()  
            if filename == None or filename == '':  
                break
            # 接收文件大小（可选）  
            filesize = int.from_bytes(client_socket.recv(8), byteorder='big')  
    
            # 接收图片数据并保存  
            print(f'----------- {filename} received and saved.') 
            with open("./pic/"+filename, 'wb') as f:  
                while filesize > 0:  
                    data = client_socket.recv(4096)  
                    f.write(data)  
                    filesize -= len(data)  
    
            # print(f'Image {filename} received and saved.')  
        if flag:
            client_socket.close()
  
# 使用示例  
# receive_image('localhost', 12345)

t=threading.Thread(target=tcplink,args=('192.168.1.170', 11000))
t.setDaemon(True)  # <-- add this
t.start()

while True:
    import time
    time.sleep(1)