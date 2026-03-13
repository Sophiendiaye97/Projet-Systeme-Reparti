import socket
import json
import time
import random

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def collect_metrics():
    return {
        "cpu": random.randint(0,100),
        "memory": random.randint(0,100),
        "disk": random.randint(0,100)
    }


def start_client(node_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    print(f"[CLIENT {node_id}] connecté")

    while True:
        data = collect_metrics()

        message = {
            "node": node_id,
            "metrics": data
        }

        client.send(json.dumps(message).encode())

        time.sleep(3)


if __name__ == "__main__":
    start_client("node2") 






    