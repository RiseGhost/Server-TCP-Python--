import sys, socket
from threading import Thread, Event

server_ip, port = '192.168.206.39', 8080 #PUT YOU IP HERE
ConnectList = []

def SendMSG(connect):
    try:
        data = connect.recv(1024)       #1024 is the max msg bytes
        for SockectClient in ConnectList:
            if (SockectClient != connect): SockectClient.send(data)
        if (len(ConnectList) == 1): ConnectList[0].send(b"You are alone")
        SendMSG(connect)
    except:
        print("Err ❌\nProbably the client disconnected")
        ConnectList.remove(connect)

def WaitForClients(server_socket, event):
    while not event.is_set():
        try:
            connect, ip_address = server_socket.accept()
            ConnectList.append(connect)
            print("Client connect 🔗 -> " + connect.recv(1024).decode('utf-8'))
            Thread(target=SendMSG, args=(connect,)).start() #Thread start, responsible for reading the messages from the clients and sending them to everyone
        except socket.timeout:
            continue

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen(1)
    server_socket.settimeout(5)     #In case for connect client problem, remove this line

    #Clean console:
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    #++++++++++++++++++++++
    print('Server TCP on ✅')

    event = Event()
    Thread(target=WaitForClients, args=(server_socket, event,)).start()
    
    while True:
        try:
            if (input() == "exit"):
                event.set()
                print("Server off in max 5.00s ⏱️")
                break
        except KeyboardInterrupt:
            event.set()
            print("Server off in max 5.00s ⏱️")
            break
    
    #Close connection with clients:
    for SocketConnect in ConnectList:
        SocketConnect.close()
    
main()