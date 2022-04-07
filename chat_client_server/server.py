import socket as sck
import threading as thr


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('localhost', 5000))
    client = {}


    while True:
        messaggio, indirizzo= s.recvfrom(4096)
        messaggio=messaggio.decode()
        print(messaggio)
        messaggio=messaggio.split(':')

        if messaggio[0]=="nickname":
            client[messaggio[1]]= indirizzo
            s.sendto("ok".encode(), client[messaggio[1]])
        elif messaggio[1]=="!list":
            s.sendto(f"Lista:{client.keys()}".encode(), indirizzo)
        else:
            for k in client.keys():
                if k==messaggio[1]:
                    s.sendto(f"{messaggio[1]}:{messaggio[2]}".encode(),client[k])

main()