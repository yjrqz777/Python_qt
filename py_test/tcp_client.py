import socket  
import os  
import time
def send_image(host, port, directory):  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:  
        client_socket.connect((host, port))  
  

        files_and_directories = os.listdir(directory)  
        # print(files_and_directories)
        # 打印出所有文件和文件夹  
        for item in files_and_directories:  
            # print(item)
            image_path = directory + item
            print(image_path)
        # 发送图片文件名  
            filename = os.path.basename(image_path)  
            print(filename)
            time.sleep(0.1)
            client_socket.sendall(filename.encode('utf-8'))  
    
            # 发送文件大小（可选，帮助服务端知道何时停止接收）  
            with open(image_path, 'rb') as f:  
                filesize = os.path.getsize(image_path)  
                client_socket.sendall(filesize.to_bytes(8, byteorder='big'))  
    
            # 发送图片数据  
            with open(image_path, 'rb') as f:  
                while True:  
                    data = f.read(4096)  # 每次发送4096字节  
                    if not data:  
                        break  
                    client_socket.sendall(data)  
                    # print('send data')
        client_socket.close()
        
  
# 使用示例  
send_image('127.0.0.1', 11000, './picture/')