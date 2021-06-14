import socket
import select

svr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
svr.bind(('',5555))
svr.listen(10)
socks=[svr]

while True:
    r,w,x=select.select(socks,[],[])
    for s in r:
        if s is svr:
            c,addr = svr.accept()
            socks.append(c)
        else:
            msg = s.recv(1024)
            txt = str(msg, encoding='utf-8')
            if txt != 'bye':
                for c in socks:
                    if c is not svr:
                        c.send(msg)
            else:
                print('切断要求')
                s.send(msg)
                socks.remove(s)
                s.close