import socket
import json
import time
import psutil
import platform


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

def check_ports():
    
    ports =[22, 80, 443, 3306]
    status = {}

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex(("127.0.0.1", port))

        if result ==0:
            status[port] = "open"
        else:
            status[port] = "closed"

        s.close()
        
    return status


def check_services():

    services = {
        "ssh": False,
        "nginx": False,
        "mysql": False
    }

    for proc in psutil.process__iter(['name']):
        name = proc.info['name']

        if name:
            if "ssh" in name
                services["ssh"] = True

            if "nginx" in name:
                services["nginx"] = True

            if "mysql" in name:
                services["mysql"] = True

    return services

while True:
    try:


        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage(   ).percent
        uptime = time.time() - psutil.boot_time()

        os_name = platform.system()
        processor = platform.processor()

        ports = check_ports()
        services = check_services()

        if cpu > 90:
            print(" ALERTE :CPU supérieure à 90%")

        metrics = {
            "cpu": cpu,
            "memory": memory,
            "disk": disk,
            "uptime": uptime,
            "os": os_name,
            "processor": processor,
            "services": services,
            "ports": ports,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        client = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_HOST, SERVER_PORT))

        client.send(json.dumps(metrics).encode())
        
        print("Metrics envoyées :", metrics)

        client.close()

        time.sleep(5)

        except Exception as e:
           print("Erreur :", e)
           time.sleep(5)
    
    
    
    

        






    
