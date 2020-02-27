from socket import *
import os,sys

def do_send(s,name,addr):
    while True:
        msg = input("發送：")
        if msg.strip() == "**":
            msg = "Q " + name
            s.sendto(msg.encode(),addr)
            sys.exit("離開聊天室")

        msg = "C %s %s" %(name,msg)
        s.sendto(msg.encode(),addr)

def do_recv(s):
    while True:
        data, addr = s.recvfrom(2048)
        if data.decode() == "EXIT":
            sys.exit(0)
        print(data.decode(), "\n發送：",end="")

def main():
    if len(sys.argv) < 3:
        print("error")
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("請輸入用戶名：")
        mag =  "U " + name
        s.sendto(mag.encode(),ADDR)
        
        data, addr = s.recvfrom(1024)
        if data.decode() == "ok":
            print("登錄成功,進入聊天室")
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        sys.exit("error")
    elif pid == 0:
        do_send(s,name,ADDR)
    else:
        do_recv(s)
    
if __name__ == '__main__':
    main()
