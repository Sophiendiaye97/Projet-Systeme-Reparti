import socket
import threading
import sqlite3
import json
import time



HOST = "0.0.0.0"
PORT = 5000

conn_db = sqlite3.connect("metrics.db", check_same_thread=False)
cursor = conn_db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
id INTEGER PRIMARY KEY AUTOINCREMENT,
client TEXT,
cpu REAL,
memory REAL,
disk REAL,
uptime REAL,
os TEXT,
processor TEXT,
services TEXT,
ports TEXT,
timestamp TEXT
)
""")

conn_db.commit()


def handle_client (conn, addr):

    print("Client connecté :", addr)
 
    while True:
        try:
            data = conn.recv(4096)

            if not data:
                break
            
            message = data.decode()
            metrics = json.loads(message)

            cpu = metrics.get("cpu")
            memory = metrics.get("memory")
            disk = metrics.get("disk")
            uptime = metrics.get("uptime")
            timestamp =metrics.get("time")
            os_name = metrics.get("os")
            processor = metrics.get("processor")
            services = metrics.get("services")
            ports = metrics.get("ports")

            print("\n--- Nouvelle métrique reçue ---")
            print("Client :", addr)
            print("CPU :", cpu, "%")

            if cpu > 90:
                print("ALERTE : CPU supérieure à 90%")

            print("Mémoire :", memory, "%")
            print("Disque :", disk, "%")
            print("Uptime :", uptime)
            print("Timestamp :", timestamp)
            print("OS :", os_name)
            print("Processor :", processor)
            print("Services :", services)
            print("Ports :", ports)

            print("-------------------------------")

            cursor.execute(
                "INSERT INTO metrics (client ,cpu, memory, disk, uptime, timestamp) VALUES ( ?, ?, ?, ?, ?, ?)",
                (str(addr), cpu, memory, disk, uptime, timestamp)
            )
      
            conn_db.commit()

        
        except Exception as e:
            print("Erreur :", e)
            break
     
    conn.close()


def start_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
  
    print("Serveur de supervision démarré...")


    while True:
 
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()

 



