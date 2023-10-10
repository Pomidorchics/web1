from tkinter import *
import socket

HOST = socket.gethostname()
PORT = 40810
IND = 0


def clicked():
    global IND
    IND = (IND + 1) % 4
    connection.sendall(f'{IND}'.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("", PORT))
    server.listen()
    connection, address = server.accept()
    with connection:
        print(f'Connected by {address}')
        while True:
            data = connection.recv(1024)
            connection.sendall(data)
            print(f'Recieved: {data.decode()}')
            window = Tk()
            window.title = "fghtrd"
            window.geometry('50x50')
            btn = Button(window, text="Нажмите, чтобы открыть новую картинку", command=clicked)
            btn.grid(column=0, row=0)
            window.mainloop()


