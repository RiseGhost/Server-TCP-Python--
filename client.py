import style
from ReadChat import ReadChat
from ClientConnect import ClientConnect

def main():
    style.CleanConsole()
    try:    client = ClientConnect(input("🧊 Server IP   -> "), int(input("🚪 Server PORT -> ")))
    except KeyboardInterrupt:
        print("\n\nConnection terminated by user by use CRTL + C ❎\n")
        exit()
    except ValueError:
        print("\nInvalid port ❌\nPort is a number\n")
        exit()
    try:    UserName = input("🤔 User Name   -> ")
    except KeyboardInterrupt:
        print("\n\nConnection terminated by user by use CRTL + C ❎\n")
        client.getSocket().close()
        exit()
    if (UserName != ""):    client.send(UserName)
    else:                   client.send("Null")
    LastInteraction = "Client"
    rd = ReadChat(client.getSocket(), 1024, LastInteraction)

    while True:
       try:
            if (LastInteraction == "Client"):   print("-> ", end="")
            msg = input()
            LastInteraction = "Client"
            if msg == "exit": break
            client.send(msg)
       except Exception as e:
            print(repr(e))
            break
    client.getSocket().close()
    
main()
