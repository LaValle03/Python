import qrcode

#dati nel qrcode

dati = input("Inserisci un link: ")

#settaggi iniziali del qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#aggiunta dei dati al qrcode
qr.add_data(dati)
qr.make(fit=True)

#creazione e salvataggio dell'immagine
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')

print("QrCode creato con successo")