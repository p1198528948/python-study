# 客户端
import socket
obj =socket.socket()
'''相对于客户端，制定要链接谁就好了
'''
 
obj.connect(('127.0.0.1',12000,))#链接服务端
'''
客户端去链接服务端，如果服务器端没有返回消息给客户端，则客户端会一直
在recv状态，一直等待服务器的消息
'''
 
result1= obj.recv(2014)#表示最多接收1024个字节，超过了下次接收、
result2= str(result1,encoding='utf-8')
print(result2)
while True:
    data = input('请输入你要发送的内容：')
    if data == 'q':
        obj.sendall(bytes(data, encoding='utf-8'))
        print('链接断开')
        break
    else:
        obj.sendall(bytes(data,encoding='utf-8'))
        rec_byte = obj.recv(1024)#发了之后，接收信息
        rec_str = str(rec_byte,encoding='utf-8')
        print(rec_str)
 
obj.close()#链接之后关闭