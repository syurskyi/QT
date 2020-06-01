# Echo server program
import socket

HOST = ''       # Symbolic name meaning all available interfaces
PORT = 50005    # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        text = ''
        while True:
            bin = conn.recv(1024)
            text += str(bin, 'utf8')
            if not bin or len(bin) < 1024:
                break
        print('Server got {0}'.format(text))
        text += " " + socket.gethostname() + ' ш ђ ч ћ ж љ њ '
        conn.sendall(text.encode('utf8'))
