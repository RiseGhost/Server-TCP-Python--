import sys, threading, socket

class ReadChat(threading.Thread):
    def __init__(self, serverconnect, ByteSize, Interaction):
        self.connect = serverconnect
        self.ByteSize = ByteSize
        self.ResponseNumber = 0
        self.Interaction = Interaction
        self.execute = True
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()
    
    def run(self):
        while True:
            try:
                server_response = self.connect.recv(self.ByteSize)
                sys.stdin.flush()
                self.ResponseNumber += 1
                self.Interaction = "Server"
                print(server_response.decode('utf-8') + "\n-> ", end="")
            except socket.error:
                print("\n\033[0;31mServer connection lost.\033[0m ❌\nPress ENTER to exit")
                break
            except:     break

    def getResponseNumber(self):    return self.ResponseNumber
    def getInteraction(self):       return self.Interaction