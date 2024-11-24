from socket import *
import time

def main():
    print("Starting UDP Server...UDP Receiver/Server")

    host_local = "127.0.0.1"
    port_local = 50000
    buffer_size = 1024

    server_socket = socket(family=AF_INET, type=SOCK_DGRAM)
    server_socket.bind((host_local, port_local))

    print("UDP receiver starts listening (Waiting for messages)....")

    while True:
        message, address = server_socket.recvfrom(buffer_size)
        for _ in range(10):
            print("Received message from:", address, "Message content:", message.decode(), flush=True)

        response_message = f"{message.decode()} - Received at {time.asctime()}"

        server_socket.sendto(response_message.encode(), address)

if __name__ == "__main__":
    main()
