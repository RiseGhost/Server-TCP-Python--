import sys
from ReadChat import ReadChat
from ClientConnect import ClientConnect

def main():
    #Clean console:
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    #++++++++++++++++++++++
    try:
        client = ClientConnect(input("🧊 Server IP   -> "), int(input("🚪 Server PORT -> ")))
    except KeyboardInterrupt:
        print("\n\nConnection terminated by user by use CRTL + C ❎\n")
        exit()
    UserName = input("🤔 User Name   -> ")
    if (UserName != ""):    client.send(UserName)
    else:                   client.send("Null")
    LastInteraction = "Client"
    rd = ReadChat(client.getSocket(), 1024, LastInteraction)
    
    while True:
        if (LastInteraction == "Client"):   print("-> ", end="")
        msg = input()
        LastInteraction = "Client"
        if msg == "exit": break
        client.send(msg)
    client.getSocket().close()
    
main()
