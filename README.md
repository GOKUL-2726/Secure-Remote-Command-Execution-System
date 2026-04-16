# 🔐 Secure Remote Command Execution System

## 📌 Description

This project implements a secure client-server system using TCP socket programming and SSL/TLS encryption. It allows authenticated users to execute system commands remotely and receive outputs securely over the network.

The system demonstrates secure communication, authentication, concurrency, protocol design, and logging.

---

## 🚀 Features

* 🔐 SSL/TLS secure communication
* 👥 Multi-client support using threading
* 🔑 Authentication using users.txt
* 💻 Remote command execution
* 📋 Logging system for audit tracking
* ⚡ Structured communication protocol

---

## 🏗️ Architecture

Client (CLI)
  ⬇ (SSL/TLS Encrypted Communication)
Server (Multi-threaded)
  ⬇
Command Execution
  ⬇
Log File (log.txt)

---

## 🔄 Communication Protocol

Data is transmitted in the format:

username | password | command

* Message is encoded using Base64
* Server decodes and processes the request

---

## ⚙️ Setup Instructions

### 1. Install Python

Python 3.8 or above is recommended.

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

### 4. Start Server

```
python server_ssl.py
```

---

### 5. Run Client

```
python client_ssl.py
```

---

## 🔐 Security Features

* SSL/TLS encryption ensures secure communication
* Authentication prevents unauthorized access
* Only valid users can execute commands
* Logging provides traceability

---

## 📊 Performance Evaluation

* Low response time for normal commands
* Efficient handling of multiple clients using threading
* Minimal latency under standard usage

---

## 🛠️ Error Handling

* Handles invalid login credentials
* Prevents unauthorized command execution
* Manages connection errors gracefully

---

## 📂 Project Files

* server_ssl.py → Secure server implementation
* client_ssl.py → Command-line client
* generate_cert.py → SSL certificate generator
* users.txt → Authentication data
* log.txt → Command logs
* server.crt / server.key → SSL certificate and key

---

## 🎯 Conclusion

This project successfully demonstrates a secure client-server architecture using TCP sockets with SSL/TLS encryption. It integrates authentication, logging, and concurrency to build a reliable and secure system.

---

## 🔗 GitHub Repository

https://github.com/GOKUL-2726/Secure-Remote-Command-Execution-System
