# Simple encrypted tunnel server 
import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Symmetric key - must be 16, 24 or 32 bytes for AES
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

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            decrypted = decrypt(data)
            print(f"Received (decrypted): {decrypted.decode()}")
            
            # Echo back an encrypted response
            response = f"Echo: {decrypted.decode()}".encode()
            client_socket.send(encrypt(response))
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

def server_loop(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Encrypted tunnel server listening on {host}:{port}")

    while True:
        client_sock, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    server_loop()
