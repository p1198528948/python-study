import socket

print("server start...")
sk= socket.socket()
 
sk.bind(('127.0.0.1',12000,))#绑定IP和端口，以一个元组的方式传进去
sk.listen(5)#在前面链接已经建立的情况下，后面最多让五个人等待
while True:#让服务器端处于可以永远处于接受客户端请求的状态
 
    conn,address=sk.accept()#基于conn这个链接发送东西
    conn.sendall(bytes('你好www.linuxidc.com，链接已经建立',encoding='utf-8'))#Python3要用bytes类型，发送字节
    # '''建立一次链接，服务器就先发送这个字段'''
    print(conn,address)
    while True:#让通信状态不中断
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes,encoding='utf-8')
        if ret_str =='q':#如果收到q，则终止链接
            break
        conn.sendall(bytes(ret_str+' 已收到该信息',encoding='utf-8'))
    

