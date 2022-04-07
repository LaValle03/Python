import json
import requests

i = input("0 - Frase casuale\n1 - Cerca per categoria\n2 - Cerca per testo\n")

if i == "0":
    r = requests.get("https://api.chucknorris.io/jokes/random")
    print(json.loads(r.text)['value'])
    
if i == "1":
    categorie = json.loads(requests.get("https://api.chucknorris.io/jokes/categories").text)
    
    s = ""
    for k in range(len(categorie)):
        s = s + str(k) + " - " + categorie[k] + "\n"
    
    risp = input(s)

    while int(risp) > len(categorie):
        risp = input(s)

    r = requests.get(f"https://api.chucknorris.io/jokes/random?category={categorie[int(risp)]}")
    print(json.loads(r.text)['value'])

if i == "2":
    risp = input("Inserisci una parola: ")
    
    r = requests.get(f"https://api.chucknorris.io/jokes/search?query={risp}")

    for k in json.loads(r.text)['result']:
        print(k['value'])