import socket
import base64
import ssl
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 5000

def send_data(event=None):
    user = entry_user.get()
    pwd = entry_pass.get()
    cmd = entry_cmd.get()

    if user == "" or pwd == "" or cmd == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        msg = f"{user}|{pwd}|{cmd}"
        msg = msg[::-1]
        msg = base64.b64encode(msg.encode())

        # 🔐 SSL connection
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_sock = context.wrap_socket(s, server_hostname=HOST)

        secure_sock.connect((HOST, PORT))
        secure_sock.send(msg)

        data = secure_sock.recv(65536)

        if data:
            result = base64.b64decode(data).decode()
        else:
            result = "No response"

        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state="disabled")

        secure_sock.close()

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))


def clear_data():
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")


def toggle_pass():
    if entry_pass.cget("show") == "*":
        entry_pass.config(show="")
        btn_show.config(text="Hide")
    else:
        entry_pass.config(show="*")
        btn_show.config(text="Show")


root = tk.Tk()
root.title("Secure Remote Command System")
root.geometry("600x520")

tk.Label(root, text="Secure Remote Command System",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root, width=40)
entry_user.pack(pady=5)

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, width=40, show="*")
entry_pass.pack(pady=5)

btn_show = tk.Button(root, text="Show", command=toggle_pass)
btn_show.pack(pady=5)

tk.Label(root, text="Command").pack()
entry_cmd = tk.Entry(root, width=40)
entry_cmd.pack(pady=5)

entry_cmd.bind("<Return>", send_data)

tk.Button(root, text="Run Command", command=send_data).pack(pady=5)
tk.Button(root, text="Clear Output", command=clear_data).pack(pady=5)

output_box = tk.Text(root, height=15, width=70, state="disabled")
output_box.pack(pady=10)

root.mainloop()