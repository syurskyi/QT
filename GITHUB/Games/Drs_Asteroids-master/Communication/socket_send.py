# Echo client program
import socket

HOST = 'localhost'  # The remote host
PORT = 50005        # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text2send = 'Hello world š đ č ć ž Здраво Свете'
    s.sendall(text2send.encode('utf8'))
    text = ''
    while True:
        bin = s.recv(1024)
        text += str(bin, 'utf-8')
        if not bin or len(bin) < 1024:
            break
    print('Received', text)
