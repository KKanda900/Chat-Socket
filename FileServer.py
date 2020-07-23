import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
print("socket is listening")
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Connection Recieved from {}".format(addr))
    data = conn.recv(1024)
    print("Data recieved {}".format(repr(data))

    f = open('../Data/picture.jpg', 'rb')
    l = f.read(1024)
    while True:
        conn.send(1)
        print('Sent', 1)
    f.close()

    print("Done")
    conn.send("Thanks for joining")
    conn.close()
    