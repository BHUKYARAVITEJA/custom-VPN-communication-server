# Custom Encrypted Tunnel Server (Python 3)

This project demonstrates a **simple encrypted tunnel server** implemented in Python using AES encryption. It provides a basic example of encrypted communication over TCP sockets. The server decrypts messages received from clients, prints the plaintext, and sends back an encrypted echo response.

---

## Features

- AES encryption/decryption using CBC mode with PKCS7 padding.
- TCP socket server handling multiple clients concurrently with threading.
- Basic encrypted tunnel communication, useful as an educational starting point for secure networking concepts.
- Symmetric key encryption requiring both server and client share the same secret key.

---

## Code Explanation

### Key Components

- **SECRET_KEY**: A symmetric key (16 bytes) used by AES to encrypt/decrypt data. Must be kept secret.
- **encrypt(data)**: Encrypts byte data using AES CBC mode with a random Initialization Vector (IV). Returns IV + ciphertext.
- **decrypt(data)**: Extracts the IV from incoming data and decrypts the ciphertext, returning original plaintext bytes.
- **handle_client(client_socket)**: Handles incoming client connections, continuously receiving and decrypting data, printing messages, and sending encrypted echo responses.
- **server_loop(host, port)**: Creates a socket server that listens on the specified port, accepts client connections, and spawns a new thread per client.

---

## How to Run

### Prerequisites

- Python 3 installed on your system.
- `pycryptodome` library installed (provides `Crypto` module for AES).

Install the required package:

pip install pycryptodome

