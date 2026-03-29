# 🔐 Secure Remote Command Execution System

## 📌 Description

This project implements a secure client-server system using low-level TCP socket programming and SSL/TLS encryption. It allows authenticated users to execute remote system commands securely and receive outputs over the network.

The system demonstrates concepts such as secure communication, concurrency, protocol design, authentication, and logging.

---

## 🚀 Features

* 🔐 SSL/TLS secure communication
* 👥 Multi-client support using threading
* 🔑 Authentication using users.txt
* 💻 Remote command execution with restrictions
* 📋 Logging system for audit tracking
* 🖥️ GUI client support (Tkinter)
* ⚡ Structured communication protocol

---

## 🏗️ Architecture

The system follows a client-server architecture:

Client (CLI / GUI)
  ⬇ (SSL/TLS Encrypted Communication)
Server (Multi-threaded)
  ⬇
Command Execution (subprocess)
  ⬇
Log File (log.txt)

---

## 🔄 Communication Protocol

Data is transmitted in a structured format:

username | password | command

* Message is reversed before transmission
* Encoded using Base64
* Server decodes, authenticates, and executes the command

---

## ⚙️ Setup Instructions

### 1. Install Python

Ensure Python 3.8 or above is installed.

---

### 2. Install required library

```
pip install cryptography
```

---

### 3. Generate SSL Certificates

```
python generate_cert.py
```

---

### 4. Start the Server

```
python server_ssl.py
```

---

### 5. Run Client (CLI)

```
python client_ssl.py
```

---

### 6. Run GUI Client

```
python gui_client_ssl.py
```

---

## 🔐 Security Features

* SSL/TLS encryption ensures secure communication
* Authentication prevents unauthorized access
* Command restrictions prevent unsafe execution
* Data encoding provides additional protection

---

## 📊 Performance Evaluation

The system was tested with multiple concurrent clients.

* Response Time: Low for standard commands
* Concurrency: Efficient due to threading
* Scalability: Handles multiple clients simultaneously
* Latency: Minimal under normal conditions

---

## 🛠️ Optimization & Error Handling

* Handles invalid credentials
* Restricts unauthorized commands
* Uses exception handling for network errors
* Supports multiple clients concurrently
* Ensures stable server operation

---

## 📂 Project Files

* server_ssl.py → Secure multi-threaded server
* client_ssl.py → Command-line client
* gui_client_ssl.py → GUI client
* generate_cert.py → SSL certificate generator
* users.txt → Authentication data
* log.txt → Command logs
* server.crt / server.key → SSL certificates

---

## 🎯 Conclusion

This project successfully demonstrates a secure network application using TCP sockets and SSL/TLS encryption. It integrates authentication, concurrency, protocol design, and logging to provide a complete and reliable system.

---

## 🔗 GitHub Repository

https://github.com/GOKUL-2726/Secure-Remote-Command-Execution-System
