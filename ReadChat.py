import sys, threading

class ReadChat(threading.Thread):
    def __init__(self, serverconnect, ByteSize, Interaction):
        self.connect = serverconnect
        self.ByteSize = ByteSize
        self.ResponseNumber = 0
        self.Interaction = Interaction
        self.execute = True
        threading.Thread.__init__(self)
        self.start()
    
    def run(self):
        while True:
            try:
                server_response = self.connect.recv(self.ByteSize)
                sys.stdin.flush()
                self.ResponseNumber += 1
                self.Interaction = "Server"
                print(server_response.decode('utf-8') + 
                      "\n-> ", end="")
            except:     break

    def getResponseNumber(self):    return self.ResponseNumber
    def getInteraction(self):       return self.Interaction