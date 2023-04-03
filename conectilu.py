import time
import socket

PORT = 4999  # Port to listen on (non-privileged ports are > 1023)

def conection(HOST):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.connect(server_address)
    return sock



def send_command_teste(comando, sock):
    
    sock.sendall(comando)
    sock.settimeout(2)
    res = ""
    
    x = 0

    while True:
        try:
            buffer = sock.recv(150).decode('utf-8')
            res+=(buffer)
            x=x+1
        except socket.timeout:
            if x == 0:
                print("Erro")
                break
                return [-1, ""]
            else:
                break

    print(res)
    #buffer_array = buffer.split(",")
    #print(buffer_array[8])
    return [1, res]

