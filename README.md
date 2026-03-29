# 🔐 Secure Remote Command Execution System

## 📌 Description
This project implements a secure client-server system using TCP socket programming and SSL/TLS encryption. It allows authenticated users to execute remote system commands and receive outputs securely over the network.

---

## 🚀 Features
- 🔐 SSL/TLS secure communication
- 👥 Multi-client support using threading
- 🔑 Authentication using users.txt
- 💻 Remote command execution with restrictions
- 📋 Logging system for audit tracking
- 🖥️ GUI client support (Tkinter)
- ⚡ Structured communication protocol

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

- Message is reversed and Base64 encoded before sending
- Server decodes, verifies, and processes the request securely

---

## ⚙️ Setup Instructions

### 1. Install Python
Ensure Python is installed (Python 3.8+ recommended)

### 2. Install required library
