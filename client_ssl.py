import socket
import base64
import ssl

HOST = '127.0.0.1'
PORT = 5000

username = input("Enter username: ")
password = input("Enter password: ")
command = input("Enter command: ")

msg = f"{username}|{password}|{command}"
msg = msg[::-1]
msg = base64.b64encode(msg.encode())

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_sock = context.wrap_socket(sock, server_hostname=HOST)

try:
    secure_sock.connect((HOST, PORT))
    secure_sock.send(msg)

    data = secure_sock.recv(4096)
    result = base64.b64decode(data).decode()

    print("\nServer Output:\n", result)

except Exception as e:
    print("Error:", e)

finally:
    secure_sock.close()