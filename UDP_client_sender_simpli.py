from socket import *
import time

def main():
    server_host = '127.0.0.1'
    server_port = 50000
    buffer_size = 1024

    client_socket = socket(family=AF_INET, type=SOCK_DGRAM)

    message = "Lila"

    start_time = time.time()

    try:
        for _ in range(10):
            client_socket.sendto(message.encode(), (server_host, server_port))

            response, server_address = client_socket.recvfrom(buffer_size)
            print("Response from server:", response.decode())

            total_bytes = len(message.encode())
            transmission_time = time.time() - start_time
            throughput = total_bytes / transmission_time if transmission_time > 0 else 0
            print(f"Throughput: {throughput:.2f} bytes/second")

    except Exception as e:
        print(f"An error happened: {e}")

    client_socket.close()

if __name__ == "__main__":
    main()
