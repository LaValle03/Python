import flask
import sqlite3
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#WEBPI che trova l'indirizzo a partire dall'id dell'autovelox
@app.route('/cerca1', methods=['GET'])
def cerca1():
    id_autovelox = request.args['id_autovelox']

    #connessione con il DB e lettura dell'indirizzo
    database = sqlite3.connect('verifica/db.db')
    cursore = database.cursor()
    indirizzo = cursore.execute(f"SELECT indirizzo FROM autovelox WHERE id_autovelox = '{id_autovelox}'").fetchall()
    database.close()

    if len(indirizzo) == 0:
        return "Nessun indirizzo trovato"
    return indirizzo[0][0]

#WEBPI che inserisce una righa nella tabella REGISTRAZIONI attraverso alcuni dati passati con la GET
@app.route('/carica', methods=['GET'])
def carica():
    targa = request.args['targa']
    velocita = int(request.args['velocita'])
    data_ora = request.args['data'] + " " + request.args['ora']
    id_autovelox = request.args['id_autovelox']

    #connessione con il DB
    database = sqlite3.connect('verifica/db.db')
    cursore = database.cursor()

    #controllo che l'id dell'autovelox esista all'interno della tabella AUTOVELOX
    query = cursore.execute(f"SELECT id_autovelox FROM autovelox WHERE id_autovelox = '{id_autovelox}'").fetchall()

    #se l'id non esiste il codice si interrompe prima di scrivere sul DB
    if len(query) == 0:
        return "ID dell'autovelox non valido"
    
    #scrittura sul DB della registrazione
    cursore.execute(f"INSERT INTO registrazioni (targa, velocita, data_ora, id_autovelox) VALUES ('{targa}',{velocita},'{data_ora}','{id_autovelox}')")
    database.commit()
    database.close()

    return "OK";

#WEBPI che trova le targhe a partire dall'indirizzo e dalla velocita massima consentita
@app.route('/trovaAuto', methods=['GET'])
def trovaAuto():
    id_autovelox = request.args['id_autovelox']
    velocita = int(request.args['velocita'])

    #connessione con il DB e lettura delle targhe
    database = sqlite3.connect('verifica/db.db')
    cursore = database.cursor()
    targhe = cursore.execute(f"SELECT targa FROM registrazioni WHERE id_autovelox = '{id_autovelox}' AND velocita > {velocita}").fetchall()
    database.close()

    #utlizzando la funzione jsonify mando un json al client contenente diverse targhe
    return jsonify(targhe)

app.run(debug=True, host='localhost')