import socket
import subprocess
import base64
import ssl
from datetime import datetime
import threading

HOST = '127.0.0.1'
PORT = 5000

ALLOWED_COMMANDS = ["dir", "ls", "whoami", "date"]

def load_users():
    users = {}
    with open("users.txt", "r") as f:
        for line in f:
            if ":" in line:
                u, p = line.strip().split(":", 1)
                users[u] = p
    return users

def log_activity(user, cmd):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {user} executed: {cmd}\n")

def handle_client(conn, addr, users):
    print("Connected:", addr)

    try:
        data = conn.recv(4096)

        msg = base64.b64decode(data).decode()
        msg = msg[::-1]

        user, pwd, cmd = msg.split("|")

        if user in users and users[user] == pwd:

            if cmd not in ALLOWED_COMMANDS:
                result = "Command not allowed"
            else:
                result = subprocess.getoutput(cmd)
                log_activity(user, cmd)

        else:
            result = "Authentication Failed"

        conn.send(base64.b64encode(result.encode()))

    except Exception as e:
        conn.send(base64.b64encode(str(e).encode()))

    finally:
        conn.close()


def start_server():
    users = load_users()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    print("Secure Server running on port", PORT)

    while True:
        client, addr = sock.accept()
        secure_conn = context.wrap_socket(client, server_side=True)

        thread = threading.Thread(target=handle_client, args=(secure_conn, addr, users))
        thread.start()


if __name__ == "__main__":
    start_server()
    
