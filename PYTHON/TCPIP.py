# coding=utf-8
import tkinter as tk  # 導入 tkinter as tk
import socket
import os
import sys

def resource_path(relative_path):
    #獲取程式資源絕對路徑
    try:
        # PyInstaller創建臨時資料夾,將路徑存於_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
root = tk.Tk()  # 建立tkinter 初始視窗
root.geometry("500x150+500+250")  # 視窗大小 寬x長+視窗距離螢幕x,y
root.title('TCP')  # 視窗title
root.configure(bg="#eeeeee")  # 視窗背景

def passmesg(msg):
        str = Entry1.get()
        successmesg = tk.Label(root, text='successful！', bg="#eeeeee", width=50, height=10)
        sendmesg = tk.Label(root, text='send : '+ str, bg="#eeeeee", width=50, height=10)
        responsemesg = tk.Label(root, text='response : '+ msg, bg="#eeeeee", width=50, height=10)
        successmesg.place(x=300, y=35, height=20, width=150)
        sendmesg.place(x=300, y=55, height=20, width=150)
        responsemesg.place(x=300, y=75, height=20, width=150)
def failmesg():
        failmesg = tk.Label(root, text='Error！', bg="#eeeeee", fg='#ec7070',width=50, height=10)
        failmesg.place(x=70, y=35, height=20, width=150)
        #exit.place(x=70, y=55, height=20, width=150)

def socket_client():
    str = Entry1.get()
    #macaddress = '01-' + str[0:2] + '-' + str[2:4] + '-' + str[4:6] + '-' + str[6:8] + '-' + str[8:10] + '-' + str[                                                                                                              10:12]
    HOST = '192.168.56.2'
    # HOST = socket.gethostname()
    PORT = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while len(str) != 0:
        # outdata = input('please input message: ')
        print('send: ' + str)
        s.send(str.encode())
        indata = s.recv(1024)
        if len(indata) == 0:  # connection closed
            s.close()
            print('server closed connection.')
            break
        passmesg(msg=indata.decode())
        print('recv: ' + indata.decode())
        break

def button_clear():
    Entry1.delete(0,'end')

Entry1 = tk.Entry(root)
Button1 = tk.Button(root, text='Send Msg', relief="groove",
                    bg='#ec7070',
                    activebackground='#f0a7a7',   # 設定滑鼠位於按鈕時的背景顏色
                    state=tk.NORMAL,  # 設定按鈕的狀態
                    command=lambda: [socket_client(),button_clear()]  # 執行def command
                    )
exit = tk.Button(root, text='Exit', relief="groove",
                 width=6, height=1, command=root.quit)# 關閉介面

Entry1.place(x=70, y=35, height=20, width=150)
Button1.place(x=70, y=65, height=20, width=150)
exit.place(x=70, y=95, height=20, width=150)

if __name__ == '__main__':
    root.mainloop()  # 執行tkinter視窗回圈