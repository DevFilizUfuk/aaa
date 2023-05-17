from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/mon-lien-cliquable')
def lien_cliquable():
    # Code pour récupérer l'adresse IP de la personne qui a cliqué
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    
    # Enregistrer l'adresse IP dans un fichier JSON
    data = {'ip': ip}
    with open('ips.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')
    
    # Faire quelque chose avec l'adresse IP, par exemple l'afficher
    return f"L'adresse IP est : {ip}"

if __name__ == '__main__':
    app.run()
