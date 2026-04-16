# 🔐 Secure Remote Command Execution System

## 📌 Description

This project implements a secure client-server system using TCP socket programming and SSL/TLS encryption. It allows authenticated users to execute system commands remotely and receive the output securely.

---

## 🚀 Features

* 🔐 SSL/TLS secure communication
* 👥 Multi-client support using threading
* 🔑 Authentication using users.txt
* 💻 Remote command execution
* 📋 Logging system (log.txt)
* ⚡ Structured communication protocol

---

## 🏗️ Architecture

Client
  ⬇ (SSL/TLS Encrypted Communication)
Server
  ⬇
Command Execution
  ⬇
Log File

---

## 🔄 Communication Protocol

Data is sent in the format:

username | password | command

* Encoded using Base64
* Reversed before sending
* Server decodes and processes the request

---

## ⚙️ Setup Instructions

### 1. Install Python

Python 3.8 or above is required.

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

### 4. Run Server

```
python server.py
```

---

### 5. Run Client

```
python client.py
```

---

## 🔐 Security Features

* SSL/TLS encryption ensures secure communication
* Authentication prevents unauthorized access
* Only allowed commands are executed
* Data encoding adds extra safety

---

## 📊 Performance

* Fast response time
* Supports multiple clients using threading
* Efficient communication with low latency

---

## 🛠️ Error Handling

* Handles invalid credentials
* Prevents unauthorized commands
* Handles connection errors

---

## 📂 Project Files

* server.py → Secure server implementation (uses SSL internally)
* client.py → Client program
* generate_cert.py → SSL certificate generator
* users.txt → Stores username and password
* log.txt → Stores command logs
* server.crt / server.key → SSL certificate and key

---

## 🎯 Conclusion

This project demonstrates secure client-server communication using TCP sockets with SSL/TLS encryption. It integrates authentication, command execution, and logging.

---

## 🔗 GitHub Repository

https://github.com/GOKUL-2726/Secure-Remote-Command-Execution-System
