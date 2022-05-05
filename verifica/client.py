import requests


while True:
    #menu che fa scegliere all'utente le operazioni che può fare
    scelta = input("0 --> EXIT\n1 --> TROVA INDIRIZZO\n2 --> CARICA\n3 --> TROVA TARGHE\n: ")
    
    #terminazione del programma
    if scelta == "0":
        break
    
    #utilizzo della WEBPI cerca1 per cercare l'indirizzo di un'autovelox
    if scelta == "1":
        id_autovelox = input("ID autovelox: ")
 
        indirizzo = requests.get(f"http://localhost:5000//cerca1?id_autovelox={id_autovelox}").text
        print(indirizzo)
        
    
    #utilizzo della WEBPI carica per inserire una registrazione manuale nel DB
    if scelta == "2":
        targa = input("Inserisci la targa: ")
        velocita = input("Inserisci la velocità: ")
        data = input("Inserisci la data: ")
        ora = input("Inserisci l'ora: ")
        id_autovelox = input("Inserisci l'id dell'autovelox: ")

        if velocita.isdecimal():
            risp = requests.get(f"http://localhost:5000//carica?targa={targa}&velocita={velocita}&data={data}&ora={ora}&id_autovelox={id_autovelox}").text
        else:
            risp = "Velocità o id autovelox non validi"
        
        print(risp)

    #utilizzo della WEBPI trovaAuto per cercare le targhe che hanno superato il limite di velocità
    if scelta == "3":
        id_autovelox = input("Inserisci l'id dell'autovelox: ")
        velocita = input("Inserisci la velocita massima: ")

        if velocita.isdecimal():
            targhe = requests.get(f"http://localhost:5000//trovaAuto?id_autovelox={id_autovelox}&velocita={velocita}").json()

            for k in targhe:
                print(k[0])
        else:
            print("Id o velocità non validi")