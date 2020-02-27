from socket import *
import os 

def do_chat(s,name,nl,msg):
    msg = "\n %s 說: %s " %(name,msg)
    for i  in nl:
        if i != name:
            s.sendto(msg.encode(),nl[i])

def do_quit(s,name,nl):
    msg = "\n %s 離開聊天室" %name
    for i in nl:
        if i == name:
            s.sendto(b"EXIT",nl[i])
        else:
            s.sendto(msg.encode(),nl[i])

    del nl[name]

def do_user(s,name,nl,addr):
    if (name in nl) or name == "管理員":
        s.sendto("此用戶已經存在".encode(),addr)
        return
    
    s.sendto("ok".encode(),addr)
    msg = "\n歡迎 %s 進入聊天室" %name
    for i in nl:
        s.sendto(msg.encode(),nl[i])
    nl[name] = addr 

def do_child(s,addr):
    while True:
        msg = input("管理員訊息：")
        msg = "C 管理員 " + msg
        s.sendto(msg.encode(),addr)

def do_parents(s):
    nl = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msglist = msg.decode().split(' ')
    
        if msglist[0] == "U":
            do_user(s,msglist[1],nl,addr)
        if msglist[0] == "C":
            do_chat(s,msglist[1],nl,' '.join(msglist[2:]))
        if msglist[0] == "Q":
            do_quit(s,msglist[1],nl) 

def main():
    ADDR = ("0.0.0.0",8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0 :
        print("創建多進程失敗")
    elif pid == 0 :
        do_child(s,ADDR)
    else:
        do_parents(s)

if __name__ == '__main__':
    main()