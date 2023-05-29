import sys
from ReadChat import ReadChat
from ClientConnect import ClientConnect

def main():
    #Clean console:
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    #++++++++++++++++++++++
    client = ClientConnect(input("🧊 Server IP   -> "), int(input("🚪 Server PORT -> ")))
    UserName = input("🤔 User Name   -> ")
    if (UserName != ""):    client.send(UserName)
    else:                   client.send("Null")
    LastInteraction = "Client"
    rd = ReadChat(client.getSocket(), 1024, LastInteraction)
    
    while True:
        if (LastInteraction == "Client"):   print("Write you mensage -> ", end="")
        msg = input()
        LastInteraction = "Client"
        if msg == "exit": break
        client.send(msg)
    client.getSocket().close()
    
main()
