# TCP based Sockets

import socket
import select # OS libraries capabilities
import errno # error detection
import sys

HEADER_LENGTH = 10

def encode(message):
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    return {"message": message, "message_header": message_header}

def Main():
    my_username = input("Username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((socket.gethostname(), 1234))
    client_socket.setblocking(False)
    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)

    while True:

        message = input(f'{my_username}: ')
        if message:
            message = encode(message)
            client_socket.send(message['message_header'] + message['message'])

        try:
            while True:
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()
                username_length = int(username_header.decode('utf-8').strip())
                username = client_socket.recv(username_length).decode('utf-8')
                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')
                print(f'{username}: {message}')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            continue

if __name__ == "__main__":
    Main()