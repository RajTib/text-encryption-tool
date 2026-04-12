# 🔒 Hybrid Text Encryption Tool (RSA + AES)

A Python-based encryption tool that combines the strength of RSA (asymmetric encryption) and AES (symmetric encryption) to securely encrypt and decrypt text data.

> ⚠️ Built strictly for educational purposes to understand modern encryption techniques.

---

## 🧠 Overview

This project implements a **hybrid encryption system**, where:

- AES is used for fast and efficient data encryption
- RSA is used to securely exchange the AES key

This mirrors how secure systems (like HTTPS) handle encryption in real-world applications.

---

## 🔐 How It Works

1. A random AES key is generated
2. Plaintext is encrypted using AES
3. The AES key is encrypted using RSA public key
4. Both encrypted text and encrypted key are stored/transmitted

For decryption:

1. RSA private key decrypts the AES key
2. AES key decrypts the ciphertext back to original text

---

## ⚙️ Features

- 🔒 Hybrid encryption (RSA + AES)
- 🔑 Secure key exchange using RSA
- ⚡ Fast encryption using AES
- 🔓 Decryption support for original plaintext
- 🧩 Modular and easy-to-understand implementation

---

## 🛠️ Tech Stack

- Python 🐍
- cryptography / PyCrypto / PyCryptodome 
