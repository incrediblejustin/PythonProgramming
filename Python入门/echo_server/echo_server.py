import socket
import os
import signal

def handler(a, b):
    pid, status = os.wait()
    print("pid: ", pid)
    print("status: ", status)

def do_echo(client):

    while True:

        data = client.recv(1024)
        if data:
            print("work pid: ", os.getpid())
            print("data : ", data)
            client.send(data)
        else:
            print("empty")
            break
    client.close()

def work(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(5)
    signal.signal(signal.SIGCHLD, handler)
    while True:

        while True:
            try:
                client, address = sock.accept()
                break
            except InterruptedError:
                continue

        childfd = os.fork()
        if childfd == 0:
            do_echo(client)
            os.close(childfd)
            os._exit(0)  #整个进程都退出了
            #退出子进程

        client.close()

if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, handler)
    work(8050)

