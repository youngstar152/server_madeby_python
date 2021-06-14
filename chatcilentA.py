import socket
import tkinter as tk
import tkinter.scrolledtext as tkst
import threading as th

def send (event):
    msg = e.get()
    e.delete(0,tk.END)
    if msg != 'bye':
        s.send(bytes('A: ' + msg, encoding='utf-8'))
    else:
        bye()

def bye():
    s.send(bytes('bye',encoding='utf-8'))
    win.destroy()

def recv():
    while True:
        msg = s.recv(1024)
        txt = str(msg,encoding='utf-8')
        if txt != 'bye':
            t.insert(tk.END,txt+'\n')
        else:
            break
        s.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5555))

win=tk.Tk()
e = tk.Entry(win,width=25)
e.place(x=0,y=0)
e.bind('<Return>',send)
t = tkst.Text(win)
t.place(x=0,y=20)

thread=th.Thread(target=recv)
thread.start()
win.protocol('WM_DELETE_WINDOW',bye)
win.mainloop()