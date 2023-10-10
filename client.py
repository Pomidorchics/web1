from tkinter import *
from PIL import Image, ImageTk
import socket

HOST = "192.168.0.12"
PORT = 40810
IMAGES = ["images/img1.png", "images/img2.png", "images/img3.png", "images/img4.png", "images/img5.png", "images/img6.png", "images/img7.png"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", PORT))
    client.sendall('0'.encode('utf-8'))
    while True:
        data = client.recv(1024)
        print(f"Recieved: {data.decode()}")
        img = Image.open(IMAGES[int(data.decode())])
        img.show()
