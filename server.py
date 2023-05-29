import socket, style, style
from threading import Thread, Event

server_ip, port = '192.168.1.166', 8080 #PUT YOU IP HERE
MAXBYTES = 1024                         #1024 is the max msg bytes
ConnectList = []

def CreateUserLabel(Username, UTheme, data):
    return (UTheme[0] + UTheme[1] + " " + Username + style.ResetConsoleColor + " -> " + data.decode('utf-8'))

def SendMSG(connect, Username, UserTheme):
    try:
        data = connect.recv(MAXBYTES)
        for SockectClient in ConnectList:
            try:
                if (SockectClient != connect):      SockectClient.send(CreateUserLabel(Username, UserTheme, data).encode('utf-8'))
            except Exception as e:
                print(repr(e))
        if (len(ConnectList) == 1): ConnectList[0].send(b"\033[K\r\033[0;32mServer response   -> \033[0mYou are alone")
        SendMSG(connect, Username, UserTheme)
    except:
        print("Err ❌\nProbably the client disconnected")
        ConnectList.remove(connect)

def WaitForClients(server_socket, event):
    while not event.is_set():
        try:
            connect, ip_address = server_socket.accept()
            ConnectList.append(connect)
            UserName = connect.recv(MAXBYTES)
            print("Client connect 🔗 -> " + UserName.decode('utf-8'))
            Thread(target=SendMSG, args=(connect, UserName.decode('utf-8'), style.ChoiseUserTheme(),)).start() #Thread start, responsible for reading the messages from the clients and sending them to everyone
        except socket.timeout:
            continue

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen(1)
    server_socket.settimeout(5)     #In case for connect client problem, remove this line

    style.CleanConsole()
    print('Server TCP on ✅')

    event = Event()
    Thread(target=WaitForClients, args=(server_socket, event,)).start()
    
    while True:
        try:
            if (input() == "exit"):     raise KeyboardInterrupt
        except KeyboardInterrupt:
            event.set()
            print("Server off in max 5.00s ⏱️")
            #Close connection with clients:
            for SocketConnect in ConnectList:   SocketConnect.close()
            break

main()