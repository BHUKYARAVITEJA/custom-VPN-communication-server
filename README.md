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

`pip install pycryptodome`


### Save the Code

Save the provided Python server code into a file named, for example, `vpn_server.py`.

### Run the Server

Run the script from your terminal/command prompt (not recommended inside Jupyter Notebook due to socket limitations):

`python vpn_server.py`


You will see output like:

`Encrypted tunnel server listening on 0.0.0.0:9999`


The server now waits for client connections.

---

## Example Client Code

Here is a minimal example client script that talks to the server using the same encryption protocol:

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

SECRET_KEY = b'your_16_byte_key'

def encrypt(data):
cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
return cipher.iv + ct_bytes

def decrypt(data):
iv = data[:16]
ct = data[16:]
cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
return pt

def client_program(host='127.0.0.1', port=9999):
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

try:
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        encrypted_msg = encrypt(message.encode())
        client.send(encrypted_msg)

        response = client.recv(4096)
        decrypted_response = decrypt(response)
        print("Server response:", decrypted_response.decode())
        
finally:
    client.close()

