import socket
import threading


class Classe_Thread(threading.Thread):
    def __init__(self): 
        threading.Thread.__init__(self)
        self.running = True 

    def run(self):
        while self.running:
            data, indirizzo = s.recvfrom(4096)
            print(data.decode())


def main():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    nick= input("Inserisci il tuo nickname: ")
    s.sendto((f"nickname:{nick}").encode(), ("localhost", 5000))  #invia il nick al server

    messaggio, indirizzo= s.recvfrom(4096)
    print(messaggio.decode())

    client = Classe_Thread()
    client.start()

    if messaggio.decode()=="ok":
        print("chat mode")
        while True:
            messaggio = input()
            s.sendto((f"{nick}:{messaggio}").encode(), ("localhost", 5000))
        


main()