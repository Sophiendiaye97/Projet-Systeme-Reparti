# Projet-Systeme-Reparti
Projet de Supervision dans un système réparti développé en Python.


                     INTRODUCTION
                     
Ce projet implémente un système réparti de supervision en Python.
Un serveur central reçoit des informations envoyées par plusieurs clients(noeuds) connectés au réseau.Chaque client collecte périodiquement des métriques système de sa machine et les envoie au serveur.
Le serveur reçoit ces données, les affiche dans le terminal et les enregistre dans une base de données SQLite pour permettre leur consultation.

                 ARCHITECTURE DU PROJET

Le système est composé de deux parties principales:
```
Serveur
```
```
Le serveur central:
```

 ```
.écoute sur un port réseau
.reçoit les données envoyées par les clients
.affiche les métriques dans le terminal
.enregistre les données dans une base SQLite
 ```
Clients(Nodes)
```
Les clients:
```

 ```
.collectent les métriques système
.envoient les données au serveur
 communiquent avec le serveur via Sockets
 ```

Architecture simplifiée:
```
Client1
Client2 ------> Serveur central
Client3
```
                   TECHNOLOGIES UTILISEES

Le projet utilise les technologies suivantes:
```
.Python3
.Sockets ( communication réseau)
.JSON (format des messages)
.Threads (gestion de plusieurs clients)
.SQLite3 (stockage des métriques)
 ```

                     METRIQUES COLLECTEES

Chaque client collecte les informations suivantes:
 ```
.CPU
.Mémoire
.Disque
.Uptime
.Système d'exploitation (OS)
.Processeur
.Service système
.Ports réseau
 ```

Ces métriques sont envoyées au serveur sous format JSON.

                      STRUCTURE DU PROJET

  ```
  Projet-Systeme-Reparti
  |
  |-- serveur.py
  |-- client.py
  |-- README.md
  |-- Rapport Systeme Reparti.pdf
  ```


                        FONCTIONNEMENT
```
Le serveur démarre et écoute sur un port réseau.
Les clients se connectent au serveur.
Chaque client collecte les métriques système.
Les métriques sont envoyées au serveur au format JSON.
Le serveur affiche les données reçues et les enregistre dans la base SQLite.
```
                      Exemple de sortie de serveur

Client connecté : ('127.0.0.1', 38300)

---- Nouvelle métrique reçue----
```
CPU :1.1 %
Mémoire : 47,1 %
Disque : 59,3 %
Uptime : 514.35
OS : Linux
Processor : x86_64
Services : { 'ssh': False, 'nginx' : False}
Ports : { '22' : 'closed', '80' : 'closed'}
```
                      INSTALLATION

    Cloner le projet :
    
``` 
git clone https://github.com/Sophiendiaye97/Projet-Systeme-Reparti.git
```
Se déplacer dans le dossier:

  ```
  cd Projet-Systeme-Reparti
  ```

                        EXECUTION
```
Lancer le serveur:

python3 serveur.py

Puis dans plusieurs terminaux lancer les clients:

Lancer les clients:

 python3 client.py
 python3 client.py
 python3 client.py
 ```

Pour simuler plusieurs clients, il suffit d'ouvrir plusieurs terminaux et d'exécuter client.py plusieurs fois.
Chaque instance agit comme un noeud client différent connecté au serveur.

Chaque client envoie périodiquement les métriques système au serveur central.
Le serveur traite les données reçues et les enregistre dans une base SQLite.

                         BASE DE DONNEES
                         
```
Les métriques reçues sont stokées dans une base SQLite et peuvent etre consultées avec:
      
SELECT * FROM metrics;
```

                       AUTEURS

Projet réalisé dans le cadre du cours se Systèmes Répartis (Master 1 - UNCHK)
 ```
.Ndeye Ndakhete Seck
.Khady Dite Sophie Ndiaye
.Omar Guindo
 ```
